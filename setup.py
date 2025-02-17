from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT='-e .'

def get_requirements(file_path:str) -> List[str]:
    """
    Read and return the list of requirements from the specified file.
    """
    # Read the file line by line and remove comments and blank lines.
    # Return the list of requirements.
    requirements=[]
    with open(file_path, 'r') as file:
        requirements=file.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT) 


setup(
    name='ml_proj_02',
    version='0.0.1',
    author='Vishal-Juyal-07',
    author_email='vishal.juyal@gmail.com',
    description='Machine Learning Project 02',
    url='https://github.com/Vishal-Juyal-07/ml_project_02',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)