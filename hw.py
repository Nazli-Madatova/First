class Class1:

    def First(self):
        print("Wake up.")


class Class2(Class1):

    def Second(self):
        print("Eat breakfast.")

    def First(self):
        super().First()


class Class3(Class2):

    def Third(self):
        print("Go to school.")

    def Second(self):
        super().Second()


class Class4(Class3):

    def Third(self):
        super().Third()


routine = Class2()
routine.First()

routine2 = Class3()
routine2.Second()

routine3 = Class4()
routine2.Third()
