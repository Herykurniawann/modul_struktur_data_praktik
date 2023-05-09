# stack yang menerapkan konsep doubly link list
class Node:
    def __init__(self, value):
        self.value = value
        self.lower = None
        self.higher = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.bottom = None
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.lower
        return True

    def print_from_bottom(self):
        temp = self.bottom
        while temp:
            print(temp.value)
            temp = temp.higher
        return True

    def push(self, value):
        new_node = Node(value)

        if self.height <= 0:
            self.top = new_node
            self.height = 1
            return True

        new_node.lower = self.top
        self.top = new_node
        self.top.lower.higher = self.top
        self.height += 1

        if self.height >= 2:
            temp = self.top
            while temp.lower:
                temp = temp.lower
            self.bottom = temp
        return True

    def pop(self):
        if (self.height <= 0): return None
        temp = self.top
        self.top = self.top.lower
        self.height -= 1

        if (self.height < 2):
            self.bottom = None
        return temp


if __name__ == "__main__":
    myStack = Stack(1)
    myStack.push(2)
    myStack.psuh(3)
    myStack.print_stack()