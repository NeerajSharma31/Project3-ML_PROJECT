from setuptolls import find_packages, setup # will find all packages which is in entire ML 
from typing import List
HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    ''' THIS WILLL RETURN SETUP OF REQUIRMENTS AND RETURN THE LIST OF REQ'''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n", " ")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT
    return requirements)
setup(
    name='mlproject',
    version='0.0.1',
    auther ='NeerajSharma',
    packages= find_packages(),
    install_requires=get_requirements('requirements.txt') # it will be benifit and easy to use or not\
    # much time consuming as below code
    # install_requires=['pandas','numpy','seaborn'] # it will download this libaries automat

)