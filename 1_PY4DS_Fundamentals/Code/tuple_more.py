# tuple is similar to list: usually used for storing multiple values
# can hold values of multiple data types like list
a_list = [1, 'a', 10.5]
a_tuple = (1, 'a', 10.5)  # uses () instead of []

# using print
print(a_list)
print(a_tuple)

# supports positive and negative (integer) indexing like list
print(a_list[0], a_tuple[0])
print(a_list[-1], a_tuple[-1])


# lists are mutable: we can modify existing values in lists
# tuples are immutable: we can't modify existing values in tuples
a_list[0] = 10  # no error
# a_tuple[0] = 10  # TypeError: doesn't support item assignment


# creating tuple without parenthesis
a_tuple = (1, 'a', 10.5)
b_tuple = 1, 'a', 10.5
print(a_tuple)
print(b_tuple)


# return list or tuple
def sum_and_diff(a, b, return_list=True):
    a_sum = a + b
    a_diff = a - b
    if return_list:
        return [a_sum, a_diff]  # returns list
    else:
        return a_sum, a_diff  # returns tuple: surrounding with parenthesis is optional

print(sum_and_diff(10, 5, return_list=True))  # prints list
print(sum_and_diff(10, 5, return_list=False))  # prints tuple


# assigning individual elements to seperate variables like list
a_tuple = 1, 2
a, b = a_tuple  # num of variables must be equal to num of elements in a tuple
print(a+100, a_tuple[0]+100)
print(b+100, a_tuple[1]+100)


#
