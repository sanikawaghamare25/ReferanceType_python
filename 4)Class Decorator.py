class my_decorator():
    def __init__(self,a):
        print("inside my_decorator.__init__()")
        a()


    def __call__(self):
        print("inside my_decorator.__call__")    


@my_decorator


def a_Function():
    print("inside a Function")


print("Finished decorating a function")


a_Function()


2) program2

class Neha():
    # magic fns or dunder fus


    def __init__(self,a):
        print("Constructor")
        a()
        self.a=a;




    def __call__(self):
        print("call function")
        #print("Display fn outside class")
        #display()
        self.a()


       
@Neha
def display():
    print("Display fn outside class")


print("Last lines")
display()

