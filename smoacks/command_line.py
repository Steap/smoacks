from smoacks.sconfig import sconfig
from smoacks.structure import SmoacksStructure
from smoacks.ApiGenerator import generate_code

def main():
    my_struct = SmoacksStructure()
    print ('Setting up SMOACKS for this project with bindir: {}'.format(sconfig['structure']['bindir']))
    my_struct.renderEnvironment()

def gen():
    generate_code()
