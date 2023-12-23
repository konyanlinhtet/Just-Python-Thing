

class Human :
     planet = "Earth"#static instance
     def __init__(self, name, age):
          self.name = name
          self.age = age

     def display(self) : 
        print("name",self.name,"age", self.age, "static planet", Human.planet, "instance planet", self.planet)#variable instance

     def change_planet(self,planet):
         self.planet = planet#create variable instance
        
     @classmethod
     def class_method(cls):#class method
        print("This is class", cls.planet)#static instance 

     @staticmethod
     def static_method():#static method
         print("This is static")

h1 = Human("Mg Mg", 23)
h1.display()
h1.change_planet("Mars")
h1.display()
Human.class_method()
Human.static_method()