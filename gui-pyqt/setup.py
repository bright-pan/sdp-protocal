# ! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Administrator'

from distutils.core import setup

import py2exe
import sys

sys.argv.append('py2exe')

py2exe_options = {
    "includes":['sip','google.protobuf', 'pkg_resources'],
    "dll_excludes":["MSVCP90.dll"],
    'compressed':1,
    'optimize':2,
    'ascii':0,
    'bundle_files':1,

}
setup(
    name = 'Demo',
    version = '1.0',
    windows = ['demo.py',],
    zipfile = None,
    options = {'py2exe':py2exe_options}

)