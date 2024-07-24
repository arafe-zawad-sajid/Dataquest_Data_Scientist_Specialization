# 3.3 Defining a Class
class A:
    pass  # for defining empty class
# ---

# 3.4 Instantiating a Class
class B():
    pass
b1 = B()
print(type(b1))
# ---

# 3.5 Creating Methods
class C():
    def first_method():  # 0 positional arguments
        return 'This is my first method'
c1 = C()
# print(c1.first_method())  # TypeError: first_method() takes 0 positional arguments but 1 was given
# ---

# 3.6 Understanding 'self'
class D():
    def print_self(self):  # we can name it (self) anything
        print(self)
d1 = D()
print(d1)
d1.print_self()
D.print_self(d1)
# ---

# 3.7 Creating a Method That Accepts an Argument
class E():
    def return_list(self, input_list):
        return input_list
e1 = E()
result = e1.return_list([1, 2, 3])
print(result)
# ---
