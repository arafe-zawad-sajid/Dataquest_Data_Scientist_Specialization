import os
# os.chdir('..')
fpath = os.getcwd()+'\\artworks_clean.csv'

# 2.1 Reading our MoMA Data Set
from csv import reader

# Read the `artworks_clean.csv` file
opened_file = open(fpath, encoding='utf8')
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]

# Convert the birthdate values
for row in moma:
    birth_date = row[3]
    if birth_date != "":
        birth_date = int(birth_date)
    row[3] = birth_date

# Convert the death date values
for row in moma:
    death_date = row[4]
    if death_date != "":
        death_date = int(death_date)
    row[4] = death_date

# Convert the date values, range are already averaged in clean dataset
for row in moma:
    date = row[6]
    if date != "":
        date = int(date)
    row[6] = date
# ---

# 2.2 Calculating Artist Ages
ages = []
nobirth = 0
for row in moma:
    date = int(row[6])
    try:
        birth = int(row[3])
        age = date-birth
    except:
        nobirth+=1
        age = 0
    ages.append(age)

final_ages = []
unknown = 0
for age in ages:
    if age > 20:
        final_age = age
    else:
        unknown+=1
        final_age = 'Unknown'
    final_ages.append(final_age)
print(nobirth, unknown)
# ---

# 2.3 Converting Ages to Decades
decades = []
for age in final_ages:
    if age == 'Unknown':
        decade = 'Unknown'
    else:
        decade = str(age)
        decade = decade[:-1]
        decade += '0s'
    decades.append(decade)
# ---

# 2.4 Summarizing the Decade Data
decade_frequency = {}
for decade in decades:
    if decade not in decade_frequency:
        decade_frequency[decade] = 1
    else:
        decade_frequency[decade] += 1
# ---

# 2.6 Creating an Artist Frequency Table
artist_freq = {}
for row in moma:
    artist = row[1]
    if artist not in artist_freq:
        artist_freq[artist] = 1
    else:
        artist_freq[artist] += 1
# ---

# 2.7 Creating an Artist Summary Function
def artist_summary(artist):
    template = 'There are {count} artworks by {name} in the data set'
    output = template.format(count=artist_freq[artist], name=artist)
    return output
print(artist_summary("Henri Matisse"))
# ---

# 2.9 Challenge: Summarizing Artwork Gender Data
gender_freq = {}
for row in moma:
    gender = row[5]
    if gender not in gender_freq:
        gender_freq[gender] = 1
    else:
        gender_freq[gender] += 1

template = 'There are {c:,} artworks by {g} artists'
for gender, count in gender_freq.items():
    out = template.format(c=count, g=gender)
    print(out)
