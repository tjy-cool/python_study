class Dog(object):
    def __init__(self, name):
        self.name  = name
    
    def eat(self, food):
        print("{0} is eating...{1}".format(self.name, food))
    
d = Dog("heizi")
d.eat("fish")

choice = input(">> ")
# print(hasattr(d, choice))
# print(hasattr(d, "eat"))

def balk():
    print("babababababababa!")

if hasattr(d,choice):
    print(getattr(d, choice))
else:
    setattr(d, choice, 22)
    func = getattr(d, choice)
    # print(func)
    try :
        func()
    except TypeError:
        print(func)
    # print("%s has not the attr %s" % (d, choice ))




