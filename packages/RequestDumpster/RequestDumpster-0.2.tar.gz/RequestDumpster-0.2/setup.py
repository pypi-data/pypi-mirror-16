"""
setup packaging script for requestdumpster
"""

import os

version = "0.2"
dependencies = ['webob']

# allow use of setuptools/distribute or distutils
kw = {}
try:
    from setuptools import setup
    kw['entry_points'] = """
    [console_scripts]
    request-dumpster = requestdumpster.dumpster:main

"""
    kw['install_requires'] = dependencies
except ImportError:
    from distutils.core import setup
    kw['requires'] = dependencies

try:
    here = os.path.dirname(os.path.abspath(__file__))
    description = file(os.path.join(here, 'README.txt')).read()
except IOError:
    description = ''


setup(name='RequestDumpster',
      version=version,
      description="dump requests",
      long_description=description,
      classifiers=[], # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      author='Jeff Hammel',
      author_email='k0scist@gmail.com',
      url='http://k0s.org/hg/RequestDumpster',
      license='',
      packages=['requestdumpster'],
      include_package_data=True,
      zip_safe=False,
      **kw
      )

