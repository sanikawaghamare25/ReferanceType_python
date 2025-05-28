class Celsis:
    def __init__(self,tempreture=0):
        self.tempreture=tempreture


    def toFarenheit(self):
        return(self.tempreture*1.8)+32
   
man=Celsis()
print(man.tempreture)#get property 0
print(man.toFarenheit())#32
man.tempreture=37# set property
print(man.tempreture)#get property 37
print(man.toFarenheit())

