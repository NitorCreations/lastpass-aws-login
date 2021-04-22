"""setuptools installation script"""
import io
from os import path

from setuptools import setup, find_packages


with io.open(path.join(path.abspath(path.dirname(__file__)), 'README.md'),
             encoding='utf-8') as readme:
    LONG_DESCRIPTION = readme.read()

setup(
    name='lastpass-aws-login',
    version="0.1.0",
    description='Tool for using AWS CLI with LastPass SAML',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author="Pasi Niemi",
    author_email='pasi.niemi@nitor.com',
    url='https://github.com/NitorCreations/lastpass-aws-login',
    license='GPLv3',
    keywords='lastpass aws awscli boto3',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[
        'threadlocal-aws==0.8',
        'requests>=2.22.0"',
        'future',
    ],
    tests_require=[
        "pytest==4.6.5",
        "pytest-mock==1.10.4",
        "pytest-cov==2.7.1",
        "requests-mock==1.6.0",
        "pytest-runner",
        "mock==3.0.5",
        "cryptography==3.3.2",
    ],
    test_suite="tests",
    entry_points={
        'console_scripts': [
            'lastpass-aws-login=aws_lp.main:main'
        ]
    },
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ]
)
