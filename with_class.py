class Flower:

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def smell(self):
        print("Flower " + self.name + " smells " + self.type)

    def edible(self):
        if self.name == "ummetta":
            return False
        elif self.name == "cabbage":
            return True
        else:
            return False
    
    def _characters(self):
        if self.name == "ummetta":
            print("ummetta colour is white, mostly grows in out fields")
        elif self.name == "cabbage":
            print("cabbage colour also white & green, grows in yards & gardren, fields")
        else:
            print(self.name + " characters not found.")


if __name__ == "__main__":
    obj = Flower("ummetta", "bad")
    print(obj.edible())
    obj.smell()
