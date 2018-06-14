#!/usr/bin/env python
#
# python-mtp setup script
# Setup.py for python-mtp
#
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import platform

setup(
	name = "mtp",
	version = "1.0.1",
	platforms = [platform.machine()],
	license = 'GPLv3',
	description = "libmtp bindings for Python",
	long_description='''libmtp bindings for Python''',
	cmdclass = {'build_ext': build_ext},
	ext_modules = [Extension('mtp', ['mtp.pyx', 'libmtp.pxd', ],
		libraries=['mtp', ],
		include_dirs=['/usr/include', ],
		extra_compile_args=['-Wno-cast-qual', '-Wno-unused-but-set-variable', ],
		)],
	author = "M. Dietrich",
	author_email = "mdt@pyneo.org",
	url = "http://pyneo.org/python-mtp/",
	install_requires=[
		'os',
		'datetime',
		'cython'
	]
	)
