from abc import ABC, abstractmethod
class Vehicle(ABC):

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def transmit(self):
        pass

    def sounds(self):
        pass


class Boat(Vehicle):
    
    def move(self):
        print("Boat rides on water")
    
    def transmit(self):
        print("Boat trasnsmits on gears")

class Tractor(Vehicle):

    def move(self):
        print("Tractor rides on fields")

    def transmit(self):
        print("Tractor transmits on gears")



class Driver:
    if __name__ == "__main__":
        tractor = Tractor()
        tractor.move()
        tractor.sounds()