class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self,value):
        new_node = Node(value)
        if self.root is None :
            self.root = new_node
            return True
        temp = self.root 
        while (True):
            if new_node.value == temp.value:
                return False
         