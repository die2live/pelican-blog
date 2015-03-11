Title: Install python lxml on Ubuntu
Date: 2014-07-21 09:12
Author: dai
Category: Tips
Tags: install, lxml, python, ubuntu
Slug: install-python-lxml-on-ubuntu

``` {.default .prettyprint .prettyprinted}
sudo apt-get install libxml2
sudo apt-get install libxslt1.1
sudo apt-get install libxml2-dev
sudo apt-get install libxslt1-dev
sudo apt-get install python-libxml2
sudo apt-get install python-libxslt1
sudo apt-get install python-dev
sudo apt-get install python-setuptools
sudo apt-get install cython
sudo apt-get install zlib1g-dev
```

The hypothesis is that `pip install lxml` should work in every
environment, regardless if you are using Python2 or Python3.

There's also `Cython` to be considered: You will certainly
enjoy `lxml` compiled with `Cython` due to relevant performance gains.

For reasons unknown to me, the compilation on Python2 does not find
Cython. To be more precise and absolutely explicit about this matter,
both commands below DO NOT employ Cython:

``` {.default .prettyprint .prettyprinted}
# DO NOT use these commands. I repeat: DO NOT use these commands.
$ pip-2.7 install lxml
$ easy_install-2.7 install lxml
```

So, when using Python2 you have only one alternative, as far as I know,
which is: compile from sources, Luke!

``` {.default .prettyprint .prettyprinted}
# install build environment and dependencies
$ kernel_release=$( uname -r )
$ sudo apt-get install linux-headers-${kernel_release} build-essential -y
$ sudo apt-get install libxml2-dev libxslt1-dev -y

# Download from github and compile from sources
$ git clone --branch lxml-3.2.4 https://github.com/lxml/lxml
$ python2.7 setup.py clean build --with-cython install
```

**Sources:**  

http://stackoverflow.com/questions/16149613/installing-lxml-with-pip-in-virtualenv-ubuntu-12-10-error-command-gcc-failed  

http://stackoverflow.com/questions/22239816/installing-lxml-in-virtualenv-via-pip-install-error-command-x86-64-linux-gnu-g
