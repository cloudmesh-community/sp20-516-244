#sp20-516-244 E.Cloudmesh.Common.5

from cloudmesh.common.StopWatch import StopWatch

class ECC5:

    def __init__(self):
        self.start = input('Press Enter to start')
        StopWatch.start('test')
        self.stop = input('Press Enter to stop')
        StopWatch.stop('test')
        self.time = StopWatch.get('test')

    def run(self):
        print(self.time,' second(s) have passed.')

if __name__ == '__main__':
    root = ECC5()
    root.run()