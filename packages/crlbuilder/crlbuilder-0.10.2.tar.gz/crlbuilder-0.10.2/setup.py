import os
import shutil

from setuptools import setup, find_packages, Command

import crlbuilder


class CleanCommand(Command):
    user_options = [
        ('all', None, '(Compatibility with original clean command)')
    ]

    def initialize_options(self):
        self.all = False

    def finalize_options(self):
        pass

    def run(self):
        folder = os.path.dirname(os.path.abspath(__file__))
        for sub_folder in ['build', 'dist', 'crlbuilder.egg-info']:
            full_path = os.path.join(folder, sub_folder)
            if os.path.exists(full_path):
                shutil.rmtree(full_path)


setup(
    name='crlbuilder',
    version=crlbuilder.__version__,

    description='Creates and signs X.509 certificate revocation lists (CRLs), including indirect and delta CRLs',
    long_description='Docs for this project are maintained at https://github.com/wbond/crlbuilder#readme.',

    url='https://github.com/wbond/crlbuilder',

    author='wbond',
    author_email='will@wbond.net',

    license='MIT',

    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy',

        'Topic :: Security :: Cryptography',
    ],

    keywords='crypto pki x509 certificate crl',

    install_requires=[
        'asn1crypto>=0.18.1',
        'oscrypto>=0.16.1'
    ],
    packages=find_packages(exclude=['tests*', 'dev*']),

    test_suite='dev.tests.make_suite',

    cmdclass={
        'clean': CleanCommand,
    }
)
