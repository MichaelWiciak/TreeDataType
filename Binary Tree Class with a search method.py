class Node(object):
    def __init__(self, parent, data):
        self.left = None
        self.right = None
        self.parent = parent
        self.data = data

    def append(self, data):
        if data<self.data:
            self.append_left(data)
        else:
            self.append_right(data)

    def append_left(self, data):
        if self.left is None:
            self.left = Node(self, data)
        else:
            self.left.append(data)

    def append_right(self, data):
        if self.right is None:
            self.right = Node(self, data)
        else:
            self.right.append(data)

    def display(self, indent_level=0):
        print(("  "*indent_level)+str(self.data))
        indent_level += 1
        if self.left is not None:
            self.left.display(indent_level)
        else:
            print(("  "*indent_level)+".")
        if self.right is not None:
            self.right.display(indent_level)
        else:
            print(("  "*indent_level)+".")

    def search(self, item):
        if self.data == item:
            print("We found it!")
            return True
        if item<self.data and self.left is not None:
            print(item,"is smaller than",self.data,"therefore we need to check down the left!")
            return self.left.search(item)
        elif item>self.data and self.right is not None:
            print(item,"is larger than",self.data,"therefore we need to check down the right!")
            return self.right.search(item)
        print("No possible way for the item to exist in my tree!")
        return False

