Title: Import python module with explicit path
Date: 2014-03-14 14:48
Author: dai
Category: Tips
Tags: module import, pip, python
Slug: import-python-module-with-explicit-path

Sometimes, when importing a python module into a python script, you get
error like this one  
` File "", line 1, in  ImportError: No module name package_name`

Check if that package is installed. If it is installed try using
something like:  
` import sys sys.path.append(r"/path_to_package") import package_name`
