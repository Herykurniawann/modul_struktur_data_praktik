class Node :
    def __init__ (self,value):
        self.value = value 
        self.next = None
        

class Stack :
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
        
my_stack = Stack(4)