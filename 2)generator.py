def generator(num):
    i=1
    while i<=1:
        yield(i)
        i+=1


x=generator(50)
print(x)
print(next(x))

2) program2
def createGenerator():
    n=int(input("Enter range:\n"))#5
    mylist=range(1,n+1)
    for i in mylist:
        yield i*i


myGenerator=createGenerator()
print(myGenerator)


for i in myGenerator:
    print(i,end=" ")
