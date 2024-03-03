class first:
    value2 = 170
    value3 = 100
    value = 60


class second(first):
    value = 40


class third(second):
    value2 = 50

    def __init__(self):
        print(self.value2)
        print(self.value3)
        print(self.value)


nick = third()