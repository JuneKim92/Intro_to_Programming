#This part of the code is the parent class aka the main classification of the 2 subclasses that need to be defined later. 
class Vehicle:
  #Constructor code using __init__ to initialize the attributes of the class
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __str__(self):
        return f"{self.make} {self.model}"

# This is the first child class which will be used to define the car classifcation
class Car(Vehicle):
    def __init__(self, make, model, num_doors):
      #Used super() to refer the parent vehicle class 
        super().__init__(make, model)
        self.num_doors = num_doors

    def __str__(self):
        return f"{super().__str__()}, {self.num_doors} doors"

# This is the second class which will be used to define the pick up classification
class Pickup(Vehicle):
    def __init__(self, make, model, bed_size):
        super().__init__(make, model)
        self.bed_size = bed_size

    def __str__(self):
        return f"{super().__str__()}, {self.bed_size} bed"

vehicles = []
#Choose to create a simple menu with the option to exit and show the contents of the vehicles stored in the garage
while True:
    print("Choose an option:")
    print("1. Add a car into the garage")
    print("2. Add a pickup into the garage")
    print("3. Exit and show the vehicles in the garage")

    choice = input("Enter your choice by entering 1, 2, or 3: ")

    if choice == "1":
        make = input("Enter the car's make: ")
        model = input("Enter the car's model: ")
        num_doors = input("Enter the number of doors on the car: ")
        car = Car(make, model, num_doors)
        vehicles.append(car)
        print(f"{car} has been added to the garage.")
    elif choice == "2":
        make = input("Enter the pickup's make: ")
        model = input("Enter the pickup's model: ")
        bed_size = input("Enter the bed size: ")
        pickup = Pickup(make, model, bed_size)
        vehicles.append(pickup)
        print(f"{pickup} has been added to the garage.")
    elif choice == "3":
        break
    else:
        print("Your input is invalid. Please try again with options 1, 2, or 3.")
        
print("The garage contains:")
for vehicle in vehicles:
    print(vehicle)