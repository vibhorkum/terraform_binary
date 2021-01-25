import os
import stat
import sys
import urllib.request
import zipfile
import platform


platform_type = platform.system().lower()
base_dir = os.path.dirname(__file__)
terraform_path = f'lib/terraform_{platform_type}'

if platform_type == 'windows': 
    terraform_path = f'{terraform_path}.exe'

terraform_system_executable = os.path.join(sys.prefix, terraform_path)
terraform_executable_local = os.path.join(base_dir, terraform_path)

terraform_executable = (
    terraform_system_executable
    if os.path.exists(terraform_system_executable)
    else terraform_executable_local
)

def main():
    print(terraform_executable)
    args = [] if len(sys.argv) < 2 else sys.argv[1:]
    os.execv(terraform_executable, ['terraform'] + args)
