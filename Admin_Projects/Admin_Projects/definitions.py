import os

#ref https://stackoverflow.com/questions/25389095/python-get-path-of-root-project-structure answered Aug 19 '14 at 17:42
ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # This is your Project Root

DPATH_ROOT_CURR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) \
                + "\\" \
                + "curr"#
