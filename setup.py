"""
Flask-OneID
-------------

This is the description for that library
"""
from setuptools import setup


setup(
    name='Flask-OneID',
    version='1.0.0',
    url='http://example.com/flask-sqlite3/',
    license='MIT',
    author='Odya',
    author_email='support@odya.uz',
    description='OneID integration with Flask application, (only for Uzbekistan)',
    long_description=__doc__,
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