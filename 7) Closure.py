def startAt(start): #Nested function
    def incrementBy(inc):
        return start + inc
    return incrementBy
    #return start+x


a=startAt(10)
b=startAt(20)
print(a(1),b(2))
#print(a,b)


2) program2
def outerFn(outervariable):
    print(outervariable)


    def innerFn(innervariable):
        print(innervariable)


outerFn(10)
