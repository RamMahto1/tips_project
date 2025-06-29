from setuptools import setup, find_packages
from typing import List


def get_requirements(file_path: str) -> List[str]:
    """
    this function will return a list of requirements
    """
    HYPHEN_E_DOT = '-e .'
    requirements= []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        
        ## remove any hyphen-e dot if present
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements






setup(
    name='tips_project',
    version='0.0.1',
    author='Ram',
    author_email='rammahto645@gmail.com',
    packages=find_packages(),
    istall_requires=get_requirements('requirements.txt'),
)