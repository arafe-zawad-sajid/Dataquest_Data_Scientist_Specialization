# using backslash '\' to escape a special function of characters
# we used '\' to escape the 2nd single quotation mark, which had the special function of ending the string
motto = 'Facebook\'s new motto is "move fast with stable infra."'
print(motto)

# using '*' followed by an int to concatenate a string with one or more copies of itself
# using '*' followed by a number which specifies the number of times the string has to be multiplied
name = 'sajid' * 3
print(name)

# using triple quotation ( ''' or """ ) to write strings over many lines
text = '''This is a sentence.
This is another, on a different line.
And another.'''
print(text)
# using triple quotation also allows us to use both single and double quotation marks without needing to escape them
motto = '''Facebook's new motto is "move fast with stable infra."'''
print(motto)

# example
fb_rating = 3.5
fb_rating_str = str(fb_rating)
facebook = '''Facebook's rating is '''
fb = facebook + fb_rating_str
print(fb)

# using '==' and '!=' on strings
print('Games' == 'Music')
print('Games' != 'Music')
