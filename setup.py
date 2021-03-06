from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyEX-zipline',
    version='0.0.1',
    description='Integrating zipline with pyEX',
    long_description=long_description,
    url='https://github.com/timkpaine/pyEX-zipline',
    download_url='https://github.com/timkpaine/pyEX-zipline/archive/v0.0.1.tar.gz',
    author='Tim Paine',
    author_email='timothy.k.paine@gmail.com',
    license='LGPL',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='finance data',
    packages=find_packages(exclude=[]),
)
