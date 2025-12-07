from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    Docstring for get_requirements
    :param file_path: Description
    :type file_path: str
    :return: Description
    :rtype: List[str]
'''
    requirements = []
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.strip("\n") for req in requirements if req.strip()]
    return requirements



setup(
    name="MLPROJECT",
    version="0.1.0",
    author="Shishir Khanal",
    author_email="khanals480@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)