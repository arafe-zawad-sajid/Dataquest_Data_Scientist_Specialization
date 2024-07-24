def square(num):
    return num * num
# another way to assign value
print(square(num=9))


# interfering with built-in functions: function naming
a_list = [1, 8, 10, 9, 7]
print(max(a_list))  # uses built-in func

def max(a_list):
    return "No max value returned"

max_val_test_0 = max(a_list)
print(max_val_test_0)  # uses user-definded func

del max  # deletes the function definition of max()

print(max(a_list))  # uses built-in func


# interfering with built-in functions: variable naming
sum = 5 + 12  # naming variable using built-in func name
a_list = [1, 8, 10, 9, 7]
# sum(a_list)  # TypeError: int not callable, error caused because of line 23


# initiating a parameter with default argument
def add_value(x, constant=10):  # constant is the parameter with default argument
    return x + constant

print(add_value(3))  # during func call, passing arguments to such paramter is optional
# print(add_value())  # TyperError: missing 1 positional argument

print(add_value(3, 20))  # default argument can be modified


# initiating all parameters with default arguments
def add_value(x=10, constant=10):  # x, constant are parameters with default arguments
    return x + constant

print(add_value())  # func call without passing any argument


# multiple return statements
def sum_or_diff(a, b, do_sum=True):  # using the default argument as a toggle
    if do_sum:
        return a+b
    return a-b

print(sum_or_diff(10, 5, True), sum_or_diff(10, 5, False))


# returning multiple variables 1
def sum_and_diff(a, b, return_list=False):
    if return_list:
        return [a+b, a-b]  # returned as list
    else:
        return a+b, a-b  # returned as tuple

a_tuple = sum_and_diff(10, 5, False)
print(a_tuple[0], a_tuple[1])
b_list = sum_and_diff(10, 5, True)
print(b_list[0], b_list[1])


# returning multiple variables 2
def sum_and_diff(a, b, return_list=False):
    if return_list:
        return [a+b, a-b]  # returned as list
    else:
        return a+b, a-b  # returned as tuple

a_sum, a_diff = sum_and_diff(10, 5, False)  # tuple
print(a_sum, a_diff)
a_sum, a_diff = sum_and_diff(10, 5, True)  # list
print(a_sum, a_diff)


# function without a return statement returns 'None' value
# 'None' value is an instance of 'NoneType' data type
def print_constant():
    x = 3.14  # x is defined only inside the function definition
    print(x)

j = print_constant()  # prints 3.14 from func
print(j)  # prints None
print(type(j))  # prints 'NoneType': the data type of j (None value)
# print(x)  # NameError: x is not defined

# code inside function definition not executed untill we call the function
def bad_func():
    [] / 'abc'  # will raise TypeError when bad_func() is called

print('''no error was returned because bad_func() wasn't called''')
# bad_func()  # TypeError


# memory isolation between main program and function
# global and local scope of a variable
x = 10  # global scope: available only inside the main program
y = 'test'

def print_constant():
    print(y)  # variable outside the func can be accessed inside the func
    # print(x)  # UnboundLocalError: local variable referenced before assignment
    x = 3.14  # local scope: available only inside the function
    print(x)

print_constant()
print(x)


# The local scope is always prioritized relative to the global scope
x = 10  # global scope
y = 'test'

def print_constant():
    print(y)  # prints the value of x in global scope since y is not initialized in func
    x = 3.14  # local scope
    print(x)  # prints the value of x in local scope since x is initialized in func
    z = 'local'
    print(z)

print_constant()
print(x, y)  # prints the value of x, y in global scope
# print(z)  # NameError: not defined
