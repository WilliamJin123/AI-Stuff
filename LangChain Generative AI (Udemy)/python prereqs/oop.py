# Inheritance
# Parent Class
class Car:
    def __init__(self, windows, doors, engine):
        self.windows = windows
        self.doors = doors
        self.engine = engine
    def drive(self):
        print(f"Drive {self.engine}")
        
car1 = Car(4, 5, "petrol")
car1.drive()

# Child Class

class Tesla(Car):
    def __init__(self, windows, doors, engine, selfdrive):
        super().__init__(windows, doors, engine)
        self.selfdrive = selfdrive
    def selfdriving(self):
        print(f"self driving: {self.selfdrive}")

tesla1 = Tesla(4,5,"electric", True)
tesla1.selfdriving()

tesla1.drive()

## Multiple Inheritance

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Subclass implements")
    
class Pet:
    def __init__(self, owner) -> None:
        self.owner = owner

#Derived class
class Dog(Animal, Pet):
    def __init__(self, name, owner):
        Animal.__init__(self, name)
        Pet.__init__(self, owner)
    
    def speak(self):
        return "woof"
dog = Dog("Buddy", "Krish")
print(dog.speak())
#Polymorphism
### Method Overriding

#Base class
class Shape:
    def area(self):
        return "The area of the figure"

#derived class 1
class Rect(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width*self.height
    
    
# Polymorphism with abstract base classes
from abc import ABC, abstractmethod
## Define abstract class
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

#Deriv class 1
class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"
#Deriv class 2
class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engine started"

car = Car()
motorcycle = Motorcycle()
print(car.start_engine())
print(motorcycle.start_engine())

### Encapsulation with getter / setter methods
### Public, protected, private variables
class Person:
    def __init__(self, name, age, gender) -> None:
        # self.name = name #public 
        # self.age = age #public
        self.__name = name #private
        self.__age = age #private
        self.gender = gender

## Encapsulation with getter / setter
class Person:
    def __init__(self, name, age) -> None:
        self.__name = name
        self.__age = age
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    
### Abstraction

class veh(ABC):
    def drive(self):
        print("vehicle drives")
    @abstractmethod
    def start_engine(self):
        pass
class C(veh):
    def start_engine(self):
        print("Car engine started")

def operate_veh(vehicle):
    vehicle.start_engine()
    vehicle.drive()
car = C()
operate_veh(car)

### Magic Methods
'''
__init__: initialize
__str__: str representation of object
__repr__: official str representation of object
__len__: returns length of object
__getitem__: gets an item from container
__setitem__: sets an item in container
'''
class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"{self.name}, {self.age} years old"

    def __repr__(self):
        
        return f"Person(name = {self.name}, age = {self.age})"
person = Person("Krish", 34)
print(person) # uses __str__
print(repr(person))

### Operator Overloading

# Operator	Magic Method
# +	__add__(self, other)
# –	__sub__(self, other)
# *	__mul__(self, other)
# /	__truediv__(self, other)
# //	__floordiv__(self, other)
# %	__mod__(self, other)
# **	__pow__(self, other)
# >>	__rshift__(self, other)
# <<	__lshift__(self, other)
# &	__and__(self, other)
# |	__or__(self, other)
# ^	__xor__(self, other)
# Comparison Operators:
# Operator	Magic Method
# <	__lt__(self, other)
# >	__gt__(self, other)
# <=	__le__(self, other)
# >=	__ge__(self, other)
# ==	__eq__(self, other)
# !=	__ne__(self, other)
# Assignment Operators:

# Operator	Magic Method
# -=	__isub__(self, other)
# +=	__iadd__(self, other)
# *=	__imul__(self, other)
# /=	__idiv__(self, other)
# //=	__ifloordiv__(self, other)
# %=	__imod__(self, other)
# **=	__ipow__(self, other)
# >>=	__irshift__(self, other)
# <<=	__ilshift__(self, other)
# &=	__iand__(self, other)
# |=	__ior__(self, other)
# ^=	__ixor__(self, other)
# Unary Operators:

# Operator	Magic Method
# –	__neg__(self)
# +	__pos__(self)
# ~	__invert__(self)


class Vector:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)
    def __eq__(self, other):
        return Vector(self.x == other.x and self.y == other.y)
    def __repr__(self):
        return f"Vector {self.x},{self.y}"

v1 = Vector(2,3)
v2 = Vector(4,5)
print(v1+v2)
print(v1-v2)
print(v1*3)

            
    