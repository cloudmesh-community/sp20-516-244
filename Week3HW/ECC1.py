from cloudmesh.common.util import banner, HEADING
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.variables import Variables

variables = Variables()

variables['debug'] = True
variables['trace'] = True
variables['verbose'] = 10


class ECC1:

    dictexample = {"One":"Uno","Two":"Dos","Three":"Tres"}

    def __init__(self,ban):
        self.ban = ban


    def run(self):
        banner(self.ban)
        HEADING(self.ban+"\nThis Banner is special, it tells you what function printed it!")
        print("Below is an example dictionary:\n")
        VERBOSE(self.dictexample)

if __name__ == "__main__":
    root = ECC1(input("What would you like as your banner?\n"))
    root.run()

