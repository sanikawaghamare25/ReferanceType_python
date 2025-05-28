#@dispatch-class decorator
#function decorator


def display(name):
    print("Hello " +name)


display("Rahul")
a=display # decorator function
#a("shubham")


a=print
a("Hello world")
