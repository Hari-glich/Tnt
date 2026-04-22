class vechicle:
    def vechicle_info(self):
        print("This is a vechicle")
class car(vechicle):
    def car_info(self):
        print("This is a car")

c1=car()
c1.vechicle_info()
c1.car_info()   