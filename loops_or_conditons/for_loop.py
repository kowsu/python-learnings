class ForLoop:

    def print_values(*args):
        for i in args:
            print("Current element "+ str(i))

    

if __name__ == "__main__":
    forLoop = ForLoop()
    forLoop.print_values(1,2,3,4)
    for i in range(11):
        print("current element " + str(i))
    
    list