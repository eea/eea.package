""" Installer
"""
import os
from setuptools import setup, find_packages

NAME = 'eea.package'
PATH = NAME.split('.') + ['version.txt']
VERSION = open(os.path.join(*PATH)).read().strip()

setup(name=NAME,
      version=VERSION,
      description="EEA ZopeSkel Templates",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
          "Framework :: Zope2",
          "Framework :: Zope3",
          "Framework :: Plone",
          "Framework :: Plone :: 4.3",
          "Programming Language :: Zope",
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "License :: OSI Approved :: Mozilla Public License 1.0 (MPL)",
        ],
      keywords='zopeskel template eea package',
      author='European Environment Agency',
      author_email='webadmin@eea europa eu',
      url='http://eea.github.io/docs/eea.package',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['eea'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'PasteScript',
          'ZopeSkel',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
        # These will declare what templates paster create command can find
        # -*- Entry points: -*-
        [paste.paster_create_template]
        """,
      )
