# Python 2.7
# Requires splinter and phantomjs

from splinter import Browser
import os, zipfile
from safesetup import SafeSetup

browser = Browser('phantomjs')
#browser = Browser() # Debugging - runs in Firefox

class SafeSync:
    url = ''
    username = ''
    password = ''

    def __init__(self):
        self.get_config()
        self.login()

    def get_config(self):
        setup = SafeSetup()
        (self.username, self.password) = setup.get_login()
        self.url = setup.get_safe_url()


    def login(self):
        browser.visit(self.url)

        if browser.status_code == 302:
            browser.fill('username', self.username)
            browser.fill('password', self.password)
            button = browser.find_by_name('submit')
            button.click()

        if not browser.is_text_present('Files submitted on time'):
            raise ValueError('Authentication failed')

    def submit_file(self, filepath):
        browser.attach_file('File', filepath)
        button = browser.find_by_css('input.button:nth-child(1)')
        button.click()
        self.submit_check(filepath)

    def submit_check(self, filepath):
        if not browser.is_text_present(os.path.basename(filepath)):
            raise Exception('File failed to be uploaded')

    def get_files(self, dirpath, absolute=True):
        if absolute:
            return [os.path.join(dirpath, f) for f in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath,f))]
        else:
            return [f for f in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath,f))]

    def zip_dir(self, zf, path):
        for root, dirs, files in os.walk(path):
            if '/.safe' not in root:
                for file in files:
                    zf.write(os.path.join(root, file))

    def submit_directory(self, dirpath):
        files = self.get_files(dirpath)

        for f in files:
            self.submit_file(f)

    def submit_directory_zip(self, dirpath, zip_name='dir.zip'):
        zip_path = os.path.abspath('./.safe/'+zip_name)

        zf = zipfile.ZipFile(zip_path, 'w')
        self.zip_dir(zf, dirpath)
        zf.close()

        assert(os.path.isfile(zip_path))

        self.submit_file(zip_path)
        os.remove(zip_path)

def main():
    sync = SafeSync()
    sync.submit_directory_zip('.')

if __name__ == '__main__':
    main()
