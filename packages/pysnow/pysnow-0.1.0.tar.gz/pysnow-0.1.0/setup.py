# -*- coding: utf-8 -*-

"""
pysnow
======

Python library for the ServiceNow REST API focused on ease of use and elegant syntax.

The REST API is active by default in all instances, starting with the Eureka release.

Documentation
-------------
Click `here <http://pysnow.readthedocs.org/>`_ to see the documentation

Installation
------------
# pip install pysnow


Basic usage
-----------

.. code-block:: python

   import pysnow

   # Create client object
   s = pysnow.Client(instance='myinstance',
                     user='myusername',
                     password='mypassword',
                     raise_on_empty=True)

   # Create a new record
   s.insert(table='incident', payload={'field1': 'value1', 'field2': 'value2'})

   # Create a `Request` object by querying for 'INC01234' on table 'incident'
   r = s.query(table='incident', query={'number': 'INC01234'})

   # Fetch one record and filter out everything but 'number' and 'sys_id' from the results
   res = r.get_one(fields=['number', 'sys_id'])

   # Update
   r.update({'this': 'that'})

   # Delete
   r.delete()


See the `documentation <http://pysnow.readthedocs.org/>`_ for more examples and other info

Compatibility
-------------
pysnow is compatible with both Python 2 and 3. It's been tested in Python 2.7 and Python 3.4.

Quick links
-----------

* http://wiki.servicenow.com/index.php?title=REST_API
* http://wiki.servicenow.com/index.php?title=Table_API
* http://wiki.servicenow.com/index.php?title=Tables_and_Classes
* http://wiki.servicenow.com/index.php?title=Encoded_Query_Strings
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from pysnow import __version__

setup(
    name='pysnow',
    py_modules=['pysnow'],
    version=__version__,
    description='Python library for the ServiceNow REST API',
    install_requires=['requests'],
    author='Robert Wikman',
    author_email='rbw@vault13.org',
    maintainer='Robert Wikman',
    maintainer_email='rbw@vault13.org',
    url='https://github.com/rbw0/pysnow',
    download_url='https://github.com/rbw0/pysnow/tarball/%s' % __version__,
    keywords=['servicenow', 'rest', 'api', 'http'],
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    license='GPLv2',
)