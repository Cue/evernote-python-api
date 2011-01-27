# Setup script for Evernote API package.

from setuptools import setup, find_packages


setup(
    name = 'evernote',
    version = '1.17',
    author = 'Evernote Corporation',
    author_email = 'en-support@evernote.com',
    url = 'http://www.evernote.com/about/developer/api/',
    description = 'Python bindings to the Evernote API.',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
)