import string
import random
import csv

# import string, random and csv libs
# make differetn vars for each value

letters = string.ascii_letters
num = string.digits
punctuation = string.punctuation

# function that makes 12 key password
def password_generator(length=12):
    #use f string to join var
    printable = f'{letters}{num}{punctuation}'
    #check output
    #print(type(printable))

    #convert output into a list
    printable = list(printable)

    # shuffle through the list
    random.shuffle(printable)

    random_password = random.choices(printable, k=length)
    random_password = ''.join(random_password)
    return random_password

passw = password_generator()

# add the websites name you'd be using this password for
platform = input('Website you need the password for: ')

# add a username
user = input('Username you would be using for this website: ')

# open file where you'd store the data
# append the data, so, add more info without deleting
file = open('passwords.csv', 'a', newline="")

#collect output in one var
tuple = platform, user, passw

writer = csv.writer(file)
# store data in the file
writer.writerow(tuple)
file.close()
