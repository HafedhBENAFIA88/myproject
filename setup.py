from setuptools import find_packages,setup
from typing import List
import os

def get_requirements(path:str)->List[str]:
 
    '''
    this functio returns the list of requirements
 
    '''
    hyphen_e_dot='-e .'
    requirements=[]
    with open(path) as obj:
      rquirements= obj.readlines()
    requirements=[req.replace('\n',"") for req in requirements]
    if hyphen_e_dot in requirements:
       requirements.remove(hyphen_e_dot)
    return requirements
      
  



setup(
name='my ML Project',
version='0.0.1',
author='Hafedh',
author_email='benafia.hafedh1988@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)