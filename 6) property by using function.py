
class Celsius:
    def __init__(self,temperature=0):
        self.temperature=temperature


    def toFarenheit(self):
        return(self.temperature*1.8)+32
   
    def get_temperature(self):
        return self.temperature
   
    def set_temperature(self,value):
        if value<-273:
            raise ValueError("Temperature below -273 is not possible")
        self.temperature=value


c=Celsius(-277)
print(c.get_temperature())
print(c.toFarenheit())
c.set_temperature(50)
print(c.get_temperature())
