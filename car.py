class Car: 
    #class variable
    car = type#class attribute
    
    def __init__(self, name, speed): #init initializes all the class attributes
        self.name = name#Instance variable
        self.speed = speed#Instance variable
        #class objects
        
car1 = Car("Volvo", "112 miles per hour or 180 Kilometers per hour ")
car2 = Car("Lamborghini", "210 t0 221 miles per hour")
car1.amount = "2000 volvo" # instance attribute, 
print(f"The speed of a {car1.name} is {car1.speed} and we have {car1.amount}, come get your car!")
        
        
        