from cloudmesh.common.Shell import Shell

class ECC4:

    def __init__(self,command):
        self.command = command

    def run(self):
        result = Shell.execute(self.command)
        print(result)

if __name__ == '__main__':
    command = input('What shell command would you like to use?\n')
    root = ECC4(command)
    root.run()



