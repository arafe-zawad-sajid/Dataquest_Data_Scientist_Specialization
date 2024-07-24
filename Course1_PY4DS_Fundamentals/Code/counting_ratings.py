from csv import reader

opened_file = open('AppleStore.csv')
read_file = reader(opened_file)
apps_data = list(read_file)


# Ex 5.7: count the number of times each unique content rating occurs in the data set
# counting technique 1: with predefining unique keys
content_ratings = {'4+': 0, '9+': 0, '12+': 0, '17+': 0}
for row in apps_data[1:]:
    c_rating = row[10]
    if c_rating in content_ratings:
        content_ratings[c_rating] += 1
print(content_ratings)


# Ex 5.8: count the number of times each unique content rating occurs in the data set while finding the unique values automatically
# counting technique 2: with empty dict, finding unique keys
content_ratings = {}
for row in apps_data[1:]:
    c_rating = row[10]
    if c_rating in content_ratings:
        content_ratings[c_rating] += 1
    else:
        content_ratings[c_rating] = 1
print(content_ratings)


# Ex 5.9: Count the number of times each unique genre occurs.
genre_counting = {}
for row in apps_data[1:]:
    genre = row[11]
    if genre in genre_counting:
        genre_counting[genre] += 1
    else:
        genre_counting[genre] = 1
print(genre_counting)
