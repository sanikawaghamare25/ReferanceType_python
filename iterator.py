1)program1
import sys
list1=list(range(1,100))
print(list1)
print(sys.getsizeof(list1))
x=iter(list1)
print(x)



2)  program2
import sys
list1=list(range(1,100))
print(list1)
print(sys.getsizeof(list1))
x=iter(list1)
print(x)
while True:
    try:
        print(next(x))
    except:
        break
print(sys.getsizeof(x))


3)program3
import sys
list1=["aishwarya","vaishnavi","sanika"]
x=iter(list1)
print(x)
while True:
    try:
        print(next(x))

    except:
        break
   # print(next(x))
print(sys.getsizeof(x))


