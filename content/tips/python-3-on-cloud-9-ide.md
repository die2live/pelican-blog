Title: Python 3 on Cloud 9 IDE
Date: 2014-06-06 10:58
Author: dai
Category: Tips
Slug: python-3-on-cloud-9-ide

The only official way to do it right now is:

``` {style="color: #333333;"}
tmux
c9pm install python3-3.3.1
c9pm install gcc-wrapper-4.6.3

pyvenv-3.3 virtualenv
```

``` {style="color: #333333;"}
cd virtualenv && source ./bin/activate
```

``` {style="color: #333333;"}
curl -O http://python-distribute.org/distribute_setup.py
python distribute_setup.py
```

``` {style="color: #333333;"}
export LD_LIBRARY_PATH=$(gcc --print-file-name=libgcc_s.so.1 | cut -d'/' -f1-5):$LD_LIBRARY_PATH
```

``` {style="color: #333333;"}
curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py
python get-pip.py
```

Enjoy!

[http://support.cloud9ide.com/entries/22898053-Python-3-support]
