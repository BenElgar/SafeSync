import os, ConfigParser, errno

class SafeSetup:
    user_config_file = os.path.expanduser("~/.safecfg")
    project_config_file = "./.safe/project.cfg"

    def make_sure_path_exists(self, path):
        try:
            os.makedirs(path)
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise

    def setup_user(self):
        print("Please note that if you continue your login details will be stored in plain text in " + self.user_config_file)
        username = raw_input("Please enter your username: ")
        password = raw_input("Please enter your password: ")

        config = ConfigParser.SafeConfigParser()
        config.add_section("Login Details")
        config.set("Login Details", "username", username)
        config.set("Login Details", "password", password)

        with open(self.user_config_file, "wb+") as configfile:
            config.write(configfile)

    def setup_project(self):
        print("Please enter the safe URL. Should be similar to https://wwwa.fen.bris.ac.uk/COMS30127/Neuron/55447/")
        safe_url = raw_input("Safe URL: ")

        config = ConfigParser.SafeConfigParser()
        config.add_section("Project Details")
        config.set("Project Details", "safe_url", safe_url)

        self.make_sure_path_exists('./.safe/')

        with open(self.project_config_file, "wb") as configfile:
            config.write(configfile)

    def get_login(self):
        try:
            config = ConfigParser.SafeConfigParser()
            config.read(self.user_config_file)
            username = config.get('Login Details', 'username')
            password = config.get('Login Details', 'password')

        except:
            self.setup_user()
            return self.get_login()

        return(username, password)

    def get_safe_url(self):
        try:
            config = ConfigParser.SafeConfigParser()
            config.read(self.project_config_file)
            url = config.get('Project Details', 'safe_url')

        except:
            self.setup_project()
            return self.get_safe_url()

        return url

    def remove_details(self):
        os.remove(self.user_config_file)
        os.remove(self.project_config_file)


def main():
    ss = SafeSetup()
    ss.setup_user()
    ss.setup_project()

if __name__ == '__main__':
    main()
