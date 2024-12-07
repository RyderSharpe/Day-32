# To run and test the code, you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explanations.

from datetime import datetime
import pandas
import random
import smtplib

# TODO 1: Update your email and password
MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"

# Get today's date
today = datetime.now()
today_tuple = (today.month, today.day)

# Read the birthdays.csv file into a pandas DataFrame
data = pandas.read_csv("birthdays.csv")

# Create a dictionary with Dictionary Comprehension to store birthdays with month and day as keys
# ------- new_dict = {new_key: new_value for (index, data_row) in data.iterrows()} -------
birthdays_dict = {(data_row.month, data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# TODO 2: Check if today matches a birthday in the birthdays.csv
if today_tuple in birthdays_dict:
    # Get the birthday person's details
    birthday_person = birthdays_dict[today_tuple]

    # TODO 3: Pick a random letter.txt file & replace the [NAME] with person's name
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    # TODO 4: Send the letter generated in step 3 to that person's email address
    with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )

# #-------------------------------------------------------------
# #To run and test the code you need to update 4 places:
# # 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# # 2. Go to your email provider and make it allow less secure apps.
# # 3. Update the SMTP ADDRESS to match your email provider.
# # 4. Update birthdays.csv to contain today's month and day.
# # See the solution video in the 100 Days of Python Course for explainations.
#
# from datetime import datetime
# import pandas
# import random
# import smtplib
#
# MY_EMAIL = "YOUR EMAIL"
# MY_PASSWORD = "YOUR PASSWORD"
#
# today = datetime.now()
# today_tuple = (today.month, today.day)
#
# data = pandas.read_csv("birthdays.csv")
# birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# if today_tuple in birthdays_dict:
#     birthday_person = birthdays_dict[today_tuple]
#     file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
#     with open(file_path) as letter_file:
#         contents = letter_file.read()
#         contents = contents.replace("[NAME]", birthday_person["name"])
#
#     with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs=birthday_person["email"],
#             msg=f"Subject:Happy Birthday!\n\n{contents}"
#         )