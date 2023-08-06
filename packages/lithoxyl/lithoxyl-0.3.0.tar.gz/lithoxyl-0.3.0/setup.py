"""A systematic approach to application instrumentation, including
logging, semantic profiling, and statistics collection. Very
lightweight, very Pythonic.

(c) 2016 by Mahmoud Hashemi.
BSD-licensed, see LICENSE for more details.

"""

import sys
from setuptools import setup, find_packages


__author__ = 'Mahmoud Hashemi'
__version__ = '0.3.0'
__contact__ = 'mahmoudrhashemi@gmail.com'
__url__ = 'https://github.com/mahmoud/lithoxyl'
__license__ = 'BSD'

desc = ('A systematic approach to logging, profiling, and statistics'
        'collection. Very lightweight, very Pythonic.')


if sys.version_info < (2,6):
    raise NotImplementedError("Sorry, lithoxyl only supports Python >=2.6")


if sys.version_info >= (3,):
    raise NotImplementedError("lithoxyl Python 3 support en route to your location")


setup(name='lithoxyl',
      version=__version__,
      description=desc,
      long_description=__doc__,
      author=__author__,
      author_email=__contact__,
      url=__url__,
      packages=find_packages(),
      install_requires=['boltons>=16.5.0'],
      include_package_data=True,
      zip_safe=False,
      license=__license__,
      platforms='any',
      classifiers=[
          'Intended Audience :: Developers',
          'Topic :: System :: Logging',
          'Topic :: Utilities',
          'Topic :: Software Development :: Libraries :: Application Frameworks',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7', ]
      )
