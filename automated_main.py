# TODO 1: Update the birthdays.csv: DONE

import smtplib
import datetime as dt
import random
import pandas


# TODO 2: Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
month = now.month
day = now.day

data = pandas.read_csv("data/birthday.csv")
print(data)

# TODO 3: If step 2 is true, pick a random letter.txt file & replace the [NAME] with person's name from birthdays.csv

# TODO 4: Send the letter generated in step 3 to that person's email address.
