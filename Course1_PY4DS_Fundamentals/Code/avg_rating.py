from csv import reader  # already imported
opened_file = open('AppleStore.csv')
read_file = reader(opened_file)
apps_data = list(read_file)

# Ex 3.1: find avg rating of free and non free apps using list, if
free_apps_ratings = []
non_free_apps_ratings = []

for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    if price == 0.0:
        free_apps_ratings.append(rating)
    else:
        non_free_apps_ratings.append(rating)

avg_rating_free = sum(free_apps_ratings) / len(free_apps_ratings)
avg_rating_non_free = sum(non_free_apps_ratings) / len(non_free_apps_ratings)
print('avg rating of free apps =', str(avg_rating_free), ', avg rating of non free apps =', str(avg_rating_non_free))


# Ex 3.4: find avg rating of gaming and non gaming apps using list, if
games_ratings = []
non_games_ratings = []

for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    if genre != 'Games':
        non_games_ratings.append(rating)
    elif genre == 'Games':
        games_ratings.append(rating)

avg_rating_non_games = sum(non_games_ratings) / len(non_games_ratings)
avg_rating_games = sum(games_ratings) / len(games_ratings)
print('avg rating of gaming apps =', str(avg_rating_games), ', avg rating of non gaming apps =', str(avg_rating_non_games))

'''On average, gaming apps have greater ratings compared to non-gaming apps.
This might be because gaming apps offer much more entertainment, which
makes the users more inclined to give higher ratings.'''


# Ex 3.5: find avg rating of free and gaming apps using list, if, and
free_games_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    genre = row[11]
    if price == 0 and genre == 'Games':
        free_games_ratings.append(rating)

avg_rating_free_games = sum(free_games_ratings) / len(free_games_ratings)


# Ex 3.6: find avg rating of apps whose genre is either Social Networking or Gaming  using list, if, or
games_social_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    if genre == 'Social Networking' or genre == 'Games':
        games_social_ratings.append(rating)

avg_games_social = sum(games_social_ratings) / len(games_social_ratings)


# Ex 3.7: find avg rating of free and non-free apps whose genre is either "Social Networking" or "Games."
free_games_social_ratings = []
nonfree_games_social_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    price = float(row[4])
    if (genre == 'Social Networking' or genre == 'Games') and price == 0:
        free_games_social_ratings.append(rating)
    elif (genre == 'Social Networking' or genre == 'Games') and price != 0:
        nonfree_games_social_ratings.append(rating)

avg_free = sum(free_games_social_ratings) / len(free_games_social_ratings)
avg_non_free = sum(nonfree_games_social_ratings) / len(nonfree_games_social_ratings)


# Ex 3.8:
# number of apps that have a price greater than $9
# avg rating of apps that have a price greater than $9
# number of apps that have a price less than or equal to $9
n_apps_all = 0
n_apps_more_9 = 0
ratings_more_9 = 0.0
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    if price > 9:
        ratings_more_9 += rating
        n_apps_more_9 += 1
    n_apps_all += 1
avg_rating = ratings_more_9 / n_apps_more_9
n_apps_less_9 = n_apps_all - n_apps_more_9
