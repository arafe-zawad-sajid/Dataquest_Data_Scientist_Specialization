# making a user definded class
class NewList():
    # 3.8 Attributes and the Init Method
    def __init__(self, initial_state):
        self.length = 0
        self.data = None

        self.calc_length(initial_state)
        self.data = initial_state

    # 3.9 Creating an Append Method
    def append(self, item):
        self.data+=[item]
        self.calc_length(item)

    # 3.10 Creating and Updating an Attribute
    def calc_length(self, item):  # helper method
        item_length = 0
        if self.data is None:
            item_length+=len(item)
        else:
            item_length+=1

        self.length += item_length


# driver code
newlist = NewList([1, 2, 3, 4, 5])
print(newlist.data)
print(newlist.length)

newlist.append(6)
print(newlist.data)
print(newlist.length)

newlist.append([7.2, '8', [9, 10]])
print(newlist.data)
print(newlist.length)
print(newlist.data[6])

print()

pylist = list([1, 2, 3, 4, 5])
print(pylist)
print(len(pylist))

pylist.append(6)
print(pylist)
print(len(pylist))

pylist.append([7.2, '8', [9, 10]])
print(pylist)
print(len(pylist))
print(pylist[6])
