from csv import reader
# open/ read/ create list
opened_file = open('AppleStore.csv')
read_file = reader(opened_file)
apps_data = list(read_file)

# creating interval
n_user_rating = []
# Step 1: generate a list of row 5 from app_data
n_user_rating = [int(row[5]) for row in apps_data[1:]]
# Step 2: find min and max from the generated list in step 1
minimum = min(n_user_rating)
maximum = max(n_user_rating)
print(minimum, maximum)
# Step 3: create frequency interval in the form of a dictionary
user_ratings_freq = {'0 - 10000': 0, '10000 - 100000': 0, '100000 - 500000': 0, '500000 - 1000000': 0, '1000000+': 0}

# computing/counting frequency for each interval
for rating in n_user_rating:
    if rating <= 10000:
        user_ratings_freq['0 - 10000'] += 1
    elif 10000 < rating < 100000:
        user_ratings_freq['10000 - 100000'] += 1
    elif 100000 < rating < 500000:
        user_ratings_freq['100000 - 500000'] += 1
    elif 500000 < rating < 1000000:
        user_ratings_freq['500000 - 1000000'] += 1
    elif rating > 1000000:
        user_ratings_freq['1000000+'] += 1

print(user_ratings_freq)
