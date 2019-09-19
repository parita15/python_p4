class Person:
    n=0;
    def __init__(self):
        Person.n=Person.n+1

    @staticmethod
    def noObject():
        print("No. of instaces created:",Person.n)

p1=Person()
Person.noObject()

