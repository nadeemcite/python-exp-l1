class A:
    def __init__(self):
        print("invoked A")

    def say_hello(self):
        print("I am hello from A")

class B(A):
    def __init__(self):
        super().__init__()
        print("invoked B")

    def say_hello(self): # this function is overriding say_hello in parent class
        print("I am hello from B")


p = B()
p.say_hello()