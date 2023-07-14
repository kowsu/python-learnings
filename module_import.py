import with_class as wc


def driver():
    instance1 = wc.Flower("ummetta", "Good")
    instance2 = wc.Flower("cabbage", "Fabulous")
    print(instance1.edible())
    print(instance2.smell())
    instance2._characters()

if __name__ == "__main__":
    driver()
