# Copyright (c) 2014, NLnet Labs, Verisign, Inc.
# All rights reserved.
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#
# *  Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# *  Neither the names of the copyright holders nor the
#    names of its contributors may be used to endorse or promote products
#    derived from this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL Verisign, Inc. BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.



from distutils.core import setup, Extension
from distutils.fancy_getopt import fancy_getopt
import platform, os, sys

long_description = ( 'getdns is a set of wrappers around the getdns'
                     'library (http://www.getdnsapi.net), providing'
                     'Python language bindings for the API')

CFLAGS = [ '-g' ]
lib_dir = ""


if '--with-getdns' in sys.argv:
    getdns_root = sys.argv[sys.argv.index('--with-getdns')+1]
    inc_dir = getdns_root + '/include'
    lib_dir = getdns_root + '/lib'
    CFLAGS.append('-I{0}'.format(inc_dir))
    sys.argv.remove('--with-getdns')
    sys.argv.remove(getdns_root)

library_dirs = [ '/usr/local/lib' ]
if lib_dir:
    library_dirs.append(lib_dir)

platform_version = list(platform.python_version_tuple())[0:2]

if not ((platform_version[0] == '3') or (platform_version == ['2', '7'])):
    print('getdns requires Python version 2.7 or Python version 3.  Exiting ... ')
    os._exit(1)

getdns_module = Extension('getdns',
                    include_dirs = [ '/usr/local/include', ],
                    libraries = [ 'getdns' ],
                    library_dirs = library_dirs,
                    sources = [ 'getdns.c', 'pygetdns_util.c', 'context.c',
                                'context_util.c', 'result.c' ],
                    extra_compile_args = CFLAGS,
                    runtime_library_dirs = library_dirs,
                    )

setup(name='getdns',
      version='v1.0.0b1',
      description='Python bindings for getdns',
      long_description=long_description,
      license='BSD',
      author='Melinda Shore',
      author_email='melinda.shore@nomountain.net',
      url='http://getdns.readthedocs.org',
      dependency_links=['git+https://github.com/getdnsapi/getdns/tree/release/v0.9.0'],
      ext_modules = [ getdns_module ],
      classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: Name Service (DNS)',
        'Topic :: Security',
        'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      keywords='DNS DNSSEC DANE',
)
