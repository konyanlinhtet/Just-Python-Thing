class Money:
    def __init__(self,value):
        self.value = value
    def __radd__(self,other):
        print("R Add called")
        return Money(self.value+other)
    def __add__(self,other):
        print("Add called")
        return Money(self.value+other.value)
   

m1 = Money(10)
m2 = Money(20)
m3 = m1 + m2 + Money(20)
print(m3.value)