from cloudmesh.common.dotdict import dotdict

class ECC2:

    def __init__(self,choice,iterable=()):
        self.__dict__.update(iterable)
        self.choice = choice

    def run(self):
        dicti = self.__dict__
        dicti = dotdict(dicti)
        if self.choice.lower() == 'blue':
            print(dicti.Blue)
        else:
            print('Wrong!')

if __name__ == "__main__":
    choice = input('What is my favorite primary color?\n')
    d = {'Blue':'Correct!','Red':'Wrong!','Yellow':'Wrong!'}
    root = ECC2(choice,d)
    root.run()