class People:

    hand = 2

    def __init__(self, name):
        self.name = name

    def work(self):
        print("%d have to work" % People.hand)

    def sleep(self):
        print("Name :", self.name, "need to sleep")
