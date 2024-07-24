# 2.5 Inserting Variables Into Strings
# using str.format()
artist = "Pablo Picasso"
birth_year = 1881

output = "{}'s birth year is {}".format(artist, birth_year)
print(output)

output = "{0}'s birth year is {1}".format(artist, birth_year)
print(output)

template = "{name}'s birth year is {year}"
output = template.format(name=artist, year=birth_year)
print(output)
# ---

# 2.8 Formatting Numbers Inside Strings
pop_millions = [
    ["China", 1379.302771],
    ["India", 1281.935991],
    ["USA", 326.625791],
    ["Indonesia", 260.580739],
    ["Brazil", 207.353391],
]
# population should have a precision of two and use a comma separator
template = 'The population of {country} is {population:,.2f} million'
for list in pop_millions:
    print(template.format(country=list[0], population=list[1]))
# ---

#
