# import reader() func of csv
from csv import reader
# open file
opened_file = open('AppleStore.csv')
# read file using reader
read_file = reader(opened_file)
# transform into list of lists
apps_data = list(read_file)
# print first 5 rows
print(apps_data[:5])
# print length (number of rows)
print(len(apps_data))  # 7198, considers the header row also


# 3.9: append a new column 'free-or_not' and append label as 'free' or 'non-free' depending on the price
apps_data[0].append('free_or_not')

for app in apps_data[1:]:
    price = float(app[4])
    if price == 0.0:
        app.append('free')
    else:
        app.append('non-free')

print(apps_data[:5])


# 3.10: append a new column 'price_label' and append label as "free," "affordable," "expensive," or "very expensive."
apps_data[0].append('price_label')

for app in apps_data[1:]:
    price = float(app[4])
    if price == 0:
        app.append('free')
    elif price > 0 and price < 20:
        app.append('affordable')
    elif price >= 20 and price < 50:
        app.append('expensive')
    elif price >= 50:
        app.append('very expensive')

print(apps_data[:5])


# Ex 5.12: Find out the minimum and the maximum app data size.
data_sizes = []
for row in apps_data[1:]:
    size = float(row[2])
    data_sizes.append(size)
min_size = min(data_sizes)
max_size = max(data_sizes)


# Ex 6.6: extract any column using a function from a list of lists
def extract(dataset, column_index):
    header_index = 0
    column_values = []
    for row in dataset[header_index+1:]:
        column_values.append(row[column_index])
    return column_values

genres = extract(apps_data, 11)  # a single list


# Ex 6.7: generate frequency table for a list
def freq_table(list_name):
    ft = {}
    for key in list_name:
        if key in ft:
            ft[key] += 1
        elif key not in ft:
            ft[key] = 1
    return ft

genres_ft = freq_table(genres)  # a single dictionary


# Ex 6.8: generate frequency table for any column with one function only
def freq_table(dataset, column_index):
    header = 0
    ft = {}
    for row in dataset[header+1:]:
        key = row[column_index]
        if key in ft:
            ft[key] += 1
        elif key not in ft:
            ft[key] = 1
    return ft

ratings_ft = freq_table(apps_data, 7)


# Ex 6.11: find sum, length then calculate mean of a column
# extract column values in a list, calculate sum and length of that list
def find_sum(a_list):
    a_sum = 0
    for element in a_list:
        a_sum += float(element)
    return a_sum

def find_length(a_list):
    length = 0
    for element in a_list:
        length += 1
    return length

def mean(data_set, column_index):
    column_values = extract(data_set, column_index)
    return find_sum(column_values) / find_length(column_values)

avg_price = mean(apps_data, 4)


# Ex 7.3: build func having parameter with default argument
# the func opens a CSV file and returns a list of lists
def open_dataset(file_name='AppleStore.csv'):
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    return data

apps_data = open_dataset()
print(apps_data[:5])


# Ex 7.5: modify open_dataset() to only return data sets without header row
def open_dataset(file_name='AppleStore.csv', has_header=True):
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    if has_header:
        return data[1:]
    return data

apps_data = open_dataset()


# Ex 7.6: modify open_dataset() to return data set rows and header row seperately in the form of tuples
def open_dataset(file_name='AppleStore.csv', header=True):
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)

    if header:
        return data[0], data[1:]  # returns a tuple of lists
    else:
        return data  # returns a list

all_data = open_dataset()
header = all_data[0]  # single list
apps_data = all_data[1]  # list of lists


# Ex 7.7: modify open_dataset() to return data set rows and header row seperately in the form of tuples
# use 2 variables to store header and apps_data seperately
def open_dataset(file_name='AppleStore.csv', header=True):
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)

    if header:
        return data[1:], data[0]
    else:
        return data

apps_data, header = open_dataset()
