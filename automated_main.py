# TODO 1: Update the birthdays.csv: DONE

import smtplib
import datetime as dt
import random
import pandas

# print(data['year'].values[0]) # Specific year
# print(data['day']) # All data from days

data = pandas.read_csv("data/birthday.csv")

# TODO 2: Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
month = now.month
today = now.day
# row_count = data['email'].count()

bday = data[(data['month'] == month) & (data['day'] == today)] # Check if its someones birthday
name = data['name'].tolist()
birthday = bday['name'].values[0]

# TODO 3: If step 2 is true, pick a random letter.txt file & replace the [NAME] with person's name from birthdays.csv

# Get ahold of the letters and assign them to variables.
with open('letter1.txt', 'r') as file:
    letter_1 = file.read()
with open('letter2.txt', 'r') as file:
    letter_2 = file.read()
with open('letter3.txt', 'r') as file:
    letter_3 = file.read()

# Randomly choose a letter to send
random_letter = random.choice((letter_1, letter_2, letter_3))

if not bday.empty:
    # print("Happy Birthday,", bday['name'].values[0])
    x = random_letter.replace('[NAME]', birthday)
    print(x)





else:
    print("No birthdays today")





# TODO 4: Send the letter generated in step 3 to that person's email address.
