def funcTree():
    print("Three")

def funcTwo():
    funcTree()
    print("Two")

def funcOne():
    funcTwo()
    print("One")

funcOne()
