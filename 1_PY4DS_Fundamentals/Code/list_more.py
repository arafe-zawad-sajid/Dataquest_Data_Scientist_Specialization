# positive indexing: first element's index = 0. increases from left to right
# negative indexing: last element's index = -1. decreases from right to left
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
print('row_1[-1] =', row_1[-1])  # last element
print('row_1[4] =', row_1[4])  # last element
print('row_1[-5] =', row_1[-5])  # first element
print('row_1[0] =', row_1[0])  # first element

# creating a new list of multiple list elements
# new list containing only the name of the app, the number of ratings and the rating
fb_rating_data = [row_1[0], row_1[-2], row_1[-1]]
print(fb_rating_data)

# list slicing: create a new list of m to n elements (upto but not including n)
# m = index of 1st element, n = index of last element + 1
list_1 = row_1[1:4]
print(list_1)
# select first x elements (x stands for a number)
first_3 = row_1[:3]  # fb price data
print(first_3)
# select last x elements (x stands for a number)
last_2 = row_1[-2:]  # fb rating data
print(last_2)

# storing multiple list variables in one list variable (data_set)
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]
data_set = [row_1, row_2, row_3, row_4, row_5]  # list storing 5 other lists
print(data_set)
# list slicing works
print(data_set[0])
print(data_set[1:3])
print(data_set[:2])
print(data_set[-2:])
# retrieving an element from a list of lists (data_set): step by step
fb_row = data_set[0]
fb_rating1 = fb_row[-1]
print(fb_rating1)
# retrieving an element from a list of lists (data_set): chaining two indices
fb_rating2 = data_set[0][-1]
print(fb_rating2)


# using '==' and '!=' on lists
print([1, 2, 3] == [1, 2, 3])
print([1, 2, 3] == [1, 2, 3, 4])


content_ratings = ['4+', '9+', '12+', '17+']
numbers = [4433, 987, 1155, 622]

# appending a list at the end of another list: 1 sub list in 1 list
content_ratings.append(numbers)
print(content_ratings)


content_ratings = ['4+', '9+', '12+', '17+']
numbers = [4433, 987, 1155, 622]

# adding lists doesn't produce list of lists:
content_rating_numbers = list(content_ratings + numbers)
print(content_rating_numbers)

# made something
content_rating_numbers = (content_ratings, numbers)
print(content_rating_numbers)

# runtime error, program quits at line of error
# content_rating_numbers = {content_ratings, numbers}  # TypeError: 'list' is unhashable

# making 1 single list of 2 lists
content_rating_numbers = [content_ratings, numbers]
print(content_rating_numbers)


# multiplying a list: list * int
a = [1, 2, 3] * 3
print(a)


# assigning individual elements to seperate variables like tuple
a_list = [1, 2]
a, b = a_list  # num of variables must be equal to num of elements in a list
print(a+100, a_list[0]+100)
print(b+100, a_list[1]+100)


# deleting a list element
a_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a_list)

del_indices = [0, 3, 4, 10]
deleted = 0
for index in del_indices:
    del a_list[index-deleted]
    deleted += 1
print(a_list)
