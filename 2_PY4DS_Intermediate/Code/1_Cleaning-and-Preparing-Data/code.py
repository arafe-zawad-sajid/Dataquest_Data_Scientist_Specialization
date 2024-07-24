import os
# os.chdir('..')
fpath = os.getcwd()+'\\artworks.csv'

# 1.1 Intro Data Cleaning
dataset = [['name', 'age', 'nationality'], ['Sajid', 23, 'Bangladeshi'], ['Fareen', 22, 'Bangladeshi'], ['Jiang', 50, 'Chinese']]
header = dataset[0]  # column title
data = dataset[1:]  # column data
print(len(data))  # number of rows
# ---

# 1.2 Reading MoMA dataset
# import the reader function from the csv module
from csv import reader

# use the python built-in function open() to open the artworks.csv file
opened_file = open(fpath, encoding='utf8')

# use csv.reader() to parse the data from the opened file
read_file = reader(opened_file)

# use list() to convert the read file into a list of lists format
moma = list(read_file)

# remove the first row of the data, which contains the column names
header = moma[0]
moma = moma[1:]
print(len(moma))
# ---

# 1.4 Cleaning the Nationality and Gender Columns
for row in moma:
    # clean parenthesis
    row[2] = row[2].replace('(', '').replace(')', '')
    row[5] = row[5].replace('(', '').replace(')', '')
# ---

# 1.5 String Capitalization
for row in moma:
    # clean empty strings, capitalize
    if not row[2]:
        row[2] = 'Nationality Unknown'
    else:
        row[2] = row[2].title()
    if not row[5]:
        row[5] = 'Gender Unknown/Other'
    else:
        row[5] = row[5].title()
# ---

# 1.6 Errors During Data Cleaning
def clean_and_convert(date):
    # check that we don't have an empty string
    if date != "":
        # move the rest of the function inside the if statement
        date = date.replace("(", "").replace(")", "")
        date = int(date)
    return date

for row in moma:
    row[3] = clean_and_convert(row[3])
    row[4] = clean_and_convert(row[4])
# ---

# 1.7 Parsing Numbers from Complex Strings, Part One
bad_chars = ["(", ")", "c", "C", ".", "s", "'", " "]
def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char, "")  # remove bad chars
    return string

# 1.8 Parsing Numbers from Complex Strings, Part Two
def process_date(date):
    if '-' in date:  # range
        d1, d2 = date.split('-')
        avg = (int(d2)+int(d1))/2
        return round(avg)
    else:  # year
        return int(date)

for row in moma:
    date = strip_characters(row[6])
    date = process_date(date)
    row[6] = date
# ---
