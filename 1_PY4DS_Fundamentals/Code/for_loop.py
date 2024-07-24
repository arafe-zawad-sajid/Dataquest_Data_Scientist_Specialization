row_0 = ['track_name', 'price', 'currency', 'rating_count_tot', 'user_rating']
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

app_data_set = [row_0, row_1, row_2, row_3, row_4, row_5]

# avoiding header
rating_sum = 0.0
for each_list in app_data_set[1:]:
    rating_sum += each_list[-1]
avg_rating = rating_sum / len(app_data_set[1:])
print(avg_rating)

# another way to find average
ratings_list = list()
for row in app_data_set[1:]:
    ratings_list.append(row[-1])
avg_rating = sum(ratings_list) / len(ratings_list)
print(avg_rating)
