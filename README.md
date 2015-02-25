These are a couple of Python classes that can be used to sync a local directory with the University of Bristol’s SAFE (System for Admin in the Faculty of Engineering).

Note that this isn’t very well tested and I doubt that it will work on Windows or OS X.

*PLEASE DO NOT USE THIS FOR FINAL SUBMISSIONS OF COURSEWORK!*

Usage
=====
My primary intention is that the files are used to build a custom system but if the safe sync file is run it will upload the current working directory to the SAFE url specified as a zip file called ‘dir.zip’.

`python2 safesync.py` - Uploads working directory to SAFE url specified

Sync Methods
-----------
`submit_file(filepath)` - Submits the specified file to SAFE. Path must be absolute.

`submit_check(filepath)` - Checks the specified file was uploaded to SAFE. Just checks that file of the same name is present on SAFE.

`submit_directory(dirpath)` - Submits all of the files in the specified directory. Does not traverse directories.

`submit_directory_zip(dirpath, zip_name=’dir.zip’)` - Submits all of the files in the specified directory as a non-compressed zip file with the name specified. If no name is specified dir.zip is used. Recursively traverses directories.

Settings Files
============
User settings are stored in the user’s home directory under ~/.safecfg
Project settings are stored in a .safe directory created in the current working directory
Both can be either manually edited or edited using safesetup.py

Dependencies
===========
* splinter
* phantomjs
