#!/usr/bin/env python
from distutils.core import setup
from distutils.command import build_py, install_data, clean
import os
import platform
import struct

# which shared library?
ulist = platform.uname()
if ulist[0] == 'Darwin':
    xpalib = 'libxpa.dylib'
    xpans = 'xpans'
elif ((ulist[0] == 'Windows') or (ulist[0].find('CYGWIN') != -1)):
    xpalib = 'libxpa.dll'
    xpans = 'xpans.exe'
else:
    xpalib = 'libxpa.so'
    xpans = 'xpans'

# make command for xpa
xpadir = 'xpa'


def make(which):
    curdir = os.getcwd()
    srcDir = os.path.join(os.path.dirname(os.path.abspath(__file__)), xpadir)
    os.chdir(srcDir)
    if which == 'all':
        os.system('echo "building XPA shared library ..."')
        cflags = ''
        if 'CFLAGS' not in os.environ and struct.calcsize("P") == 4:
            if ulist[0] == 'Darwin' or ulist[4] == 'x86_64':
                os.system('echo "adding -m32 to compiler flags ..."')
                cflags = ' CFLAGS="-m32"'
        os.system('./configure --enable-shared --without-tcl'+cflags)
        os.system('make clean; make; rm -f *.o')
    elif which == 'clean':
        os.system('echo "cleaning XPA ..."')
        os.system('make clean')
    elif which == 'mingw-dll':
        os.system('echo "building XPA shared library ..."')
        os.system('sh configure --without-tcl')
        os.system('make clean')
        os.system('make')
        os.system('make mingw-dll')
        os.system('rm -f *.o')
    os.chdir(curdir)


# rework build_py to make the xpa shared library as well
class my_build_py(build_py.build_py):
    def run(self):
        if ((platform.uname()[0] == 'Windows') or
                ((platform.uname()[0]).find('CYGWIN') != -1)):
            make('mingw-dll')
        else:
            make('all')
        build_py.build_py.run(self)


# thanks to setup.py in ctypes
class my_install_data(install_data.install_data):
    """A custom install_data command, which will install it's files
    into the standard directories (normally lib/site-packages).
    """
    def finalize_options(self):
        if self.install_dir is None:
            installobj = self.distribution.get_command_obj('install')
            self.install_dir = installobj.install_lib
        print('Installing data files to %s' % self.install_dir)
        install_data.install_data.finalize_options(self)


# clean up xpa as well
class my_clean(clean.clean):
    def run(self):
        make('clean')
        clean.clean.run(self)


# setup command
VERSION='1.8.1'
setup(name='pyds9',
      version=VERSION,
      description='Python/DS9 connection via XPA (with numpy and pyfits support)',
      author='Bill Joye and Eric Mandel',
      author_email='saord@cfa.harvard.edu',
      url='https://github.com/TESScience/pyds9/',
      download_url = 'https://github.com/TESScience/pyds9/tarball/{VERSION}'.format(VERSION=VERSION),
      keywords = ['astronomy', 'science', 'ds9'],
      py_modules=['pyds9', 'xpa'],
      data_files=[('', [os.path.join(xpadir, xpalib),
                        os.path.join(xpadir, xpans)])],
      cmdclass={'build_py': my_build_py,
                'install_data': my_install_data,
                'clean': my_clean},
      install_requires=['six'],
      )
