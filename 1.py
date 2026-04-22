from abc import ABC, abstractmethod

from inheritence import car
class shape(ABC):
    @abstractmethod
    def mileage(self):
        pass
class defender(car):
    def mileage(self):
        print("This is a defender car with 70 mileage")
class fortuner(car):
    def mileage(self):
        print("This is a fortuner car with 60 mileage")

class innova(car):
    def mileage(self):
        print("This is a innova car with 50 mileage")
d1=defender()

f1=fortuner()
f1.vechicle_info()  
print("fortuner mileage:")
f1.mileage()