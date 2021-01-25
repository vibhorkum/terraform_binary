#!/usr/bin/env python
import os
import stat
import sys
import urllib.request
import zipfile
import platform
from setuptools import setup

VERSION = '0.14.6'
TERRAFORM_VERSION = '0.14.6'

with open('README.md') as f:
    readme = f.read()

def download_terraform(platform='linux'):
    base_url = f'https://releases.hashicorp.com/terraform/{TERRAFORM_VERSION}'
    file_name = f'terraform_{TERRAFORM_VERSION}_{platform}_amd64.zip'
    download_url = f'{base_url}/{file_name}'

    download_directory = 'downloads'
    extract_directory = 'lib'
    target_file = f'{download_directory}/{file_name}'

    os.makedirs(download_directory, exist_ok=True)
    os.makedirs(extract_directory, exist_ok=True)

    if not os.path.exists(target_file):
        urllib.request.urlretrieve(download_url, target_file)

    with zipfile.ZipFile(target_file) as terraform_zip_archive:
        terraform_zip_archive.extractall(extract_directory)

    new_executable_path = f'{extract_directory}/terraform_{platform}'
    old_executable_path = f'{extract_directory}/terraform'

    if os.path.exists(new_executable_path):
        os.remove(new_executable_path)
    os.rename(old_executable_path, new_executable_path )

    executable_stat = os.stat(new_executable_path)
    os.chmod(new_executable_path, executable_stat.st_mode | 0o111)

download_terraform(platform='linux')
download_terraform(platform='darwin')

try:
    from wheel.bdist_wheel import bdist_wheel as _bdist_wheel
    class bdist_wheel(_bdist_wheel):
        def finalize_options(self):
            _bdist_wheel.finalize_options(self)
            self.root_is_pure = False
except ImportError:
    bdist_wheel = None

setup(
    name='terraform_binary',
    version=VERSION,
    long_description=readme,
    long_description_content_type='text/markdown',
    author='DevOps Team',
    author_email='',
    url='https://github.com/epiphany-platform/terraform-bin',
    license='Apache License Version 2.0',
    py_modules=['terraform'],
    data_files=[
        ('lib', ['lib/terraform_linux', 'lib/terraform_darwin'),
    ],
    entry_points={
        'console_scripts': [
            'terraform = terraform:main',
        ]
    },
)
