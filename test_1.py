class People:

    workhour = 2
    sleephour = 8

    def __init__(self, name):
        self.name = name

    def work(self):
        print(self.name,"have to work %d hours" % People.workhour)

    def sleep(self):
        print(self.name, "need to sleep", self.sleephour, "hours")
        print(f'{self.name} need to sleep {People.sleephour} hours')

