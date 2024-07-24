# dictionary keys: can be most, except lists and dictionaries
d1 = {'key': 1, 10: 2, 13.5: 3, True: 4}
print(d1)

# dictionary values: can be all, including lists and dictionaries
d2 = {1: 'string', 2: 2, 3: 3.5, 4: True, 5: [20, [3.2, 10, 40], 1.2, 'str'], 6: {.1: 'dict', .2: 22, .3: {.01: 'another dict', .02: 2.3}}}
print(d2)
print(d2[5])
print(d2[6])


# if we use identical keys, python keeps only the last key-value pair and removes the others
d2 = {'key': 1, 'key': 2, 'key': 10}
print(d2)


# python uses hash() to convert dictionary keys to int
d1 = {'key': 1, 10: 2, 13.5: 3, True: 4, False: 5}
for k in d1:
    print(hash(k))

# hash() converts boolean True to 1 and False to 0 which conflicts with int 0 and 1
d3 = {1: 'one', True: 'True', 0: 'zero', False: 'False', 2: 'two'}
print(d3)


# using 'in' operator to create a boolean exp. to check for membership
content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}
print('12+' in content_ratings)
print('13-' in content_ratings)
print(4433 in content_ratings)  # checking for a key 4433 (for values always False)


# updating dictionary values by referencing it's corresponding key
content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}
content_ratings['4+'] = 0
content_ratings['9+'] += 10
content_ratings['12+'] = 'string'
print(content_ratings)


# Ex 5.7: count the number of times each unique content rating occurs in the data set
# counting technique 1: with predefining unique keys
content_ratings = {'4+': 0, '9+': 0, '12+': 0, '17+': 0}
rating_list = ['4+', '4+', '9+', '12+', '9+', '17+', '4+']
for rating in rating_list:
    if rating in content_ratings:
        content_ratings[rating] += 1
print(rating, content_ratings)


# Ex 5.8: count while finding the unique values automatically
# counting technique 2: finding unique keys
content_ratings2 = {}
rating_list = ['4+', '4+', '9+', '12+', '9+', '17+', '4+']
for rating in rating_list:
    if rating in content_ratings2:
        content_ratings2[rating] += 1
    else:
        content_ratings2[rating] = 1
print(rating, content_ratings2)


# Ex 5.9: proportion and percentage of apps with content rating 4+
# converting frequency to proportion
proportion_4 = content_ratings['4+'] / len(rating_list)
percentage_4 = proportion_4 * 100
print(proportion_4, percentage_4)


# Ex 5.10: transform the frequencies to percentages without seperate dictionaries
content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
total_number_of_apps = 7197
for key in content_ratings:
    content_ratings[key] /= total_number_of_apps  # frequency to proportion
    content_ratings[key] *= 100  # proportion to percentage

percentage_17_plus = content_ratings['17+']
percentage_15_allowed = content_ratings['4+'] + content_ratings['9+'] + content_ratings['12+']


# Ex 5.11: transform the frequencies to proportions and percentages with separate dictionaries
content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
total_number_of_apps = 7197

c_ratings_proportions = {}
c_ratings_percentages = {}

for key in content_ratings:
    c_ratings_proportions[key] = content_ratings[key] / total_number_of_apps
    c_ratings_percentages[key] = c_ratings_proportions[key] * 100
