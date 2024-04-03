from setuptools import setup, find_packages
from typing import List


HYPEN_E_DOT = '-e .'
def get_requirements(file_name:str) -> List[str]:
    ''' returs the requirements project development environment '''
    with open(file_name, 'r') as file_obj:
        requirements = [requirement.replace('\n', '') for requirement in file_obj.readlines()]
    if (HYPEN_E_DOT in requirements) or ('' in requirements):
        requirements.remove(HYPEN_E_DOT)
        requirements.remove('')
    return requirements

PACKAGE_NAME = 'darshan_gemstone_project'
VERSION = "0.0.1"
AUTHOR_USER_NAME = 'DarshanRM'
AUTHOR_EMAIL = 'darshanrokkad2003@gmail.com'

setup(
    name = PACKAGE_NAME,
    version = VERSION,
    author = AUTHOR_USER_NAME, 
    author_email = AUTHOR_EMAIL,
    packages = find_packages(),    
    install_requires = get_requirements('requirements_dev.txt')
)