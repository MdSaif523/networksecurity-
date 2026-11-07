'''
The setup.py file is an essential part of packaging and 
distributing Python project. It is used by setup tools
(or distutils in older Python versions) to define the 
configuration of your project, such as its name, version, 
dependencies, metadata and other .
'''

from setuptools import find_packages,setup
from typing import List 

def get_requirements() -> List[str]:
    '''
    This function will return the list of requirements
    mentioned in the requirements.txt file.
    '''

    requirements_lst = []
    try:
        with open('requirements.txt','r') as file:
            # Read lines from the files.
            lines = file.readlines()
            ## process each line
            for line in lines:
                requirement = line.strip()
                # Ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirements_lst.append(requirement)

    except FileNotFoundError:
        print(f"Error: The file {'requirements.txt'} was not found.")

    return requirements_lst

setup(
    name='Network Security',
    version='0.0.1',
    author='Saifuddin',
    author_email='mds744007@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)