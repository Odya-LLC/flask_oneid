"""
Flask-OneID
-------------

This is the description for that library
"""
from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='Flask-OneID',
    version='1.0.1',
    url='https://github.com/Odya-LLC/flask_oneid',
    license='MIT',
    author='odya',
    author_email='support@odya.uz',
    description='OneID integration with Flask application, (only for Uzbekistan)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['flask_oneid'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',"requests"
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)