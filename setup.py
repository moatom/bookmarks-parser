from setuptools import setup, find_packages
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "bookmarks-parser",
    version = "0.0.1",
    author = "Tomoaki Kobayashi",
    author_emai = "tomozx8@gmail.com",
    description = "netscape bookmarks parser",
    license = "MIT",
    url = "https://github.com/moatom/bookmarks-parser",
    long_description = read('README.md'),
    packages = find_packages(exclude=('tests')),
    install_requires = ['beautifulsoup4', 'html5lib']
)
