#sp20-516-244 E.Cloudmesh.Common.3
from cloudmesh.common.FlatDict import FlatDict



class ECC3:

    def __init__(self,choice,iterable=()):
        self.choice = choice
        self.__dict__.update(iterable)

    def run(self):
        stringy = 'One.' + str(self.choice)
        flattened = FlatDict(self.__dict__,sep='.')
        return flattened[stringy]


if __name__ == '__main__':
    print('Let\'s add or subtract one from one')
    choice = input('Type either \'plus\' or \'minus\' below:\n')
    data = {'One': {'plus': 'two', 'minus': 'zero'}}
    flattened = FlatDict(data, sep='-')
    root = ECC3(choice,data)
    answer = root.run()
    print('Now we have',answer)
    print('That was fun!')