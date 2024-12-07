# Import necessary libraries for email, date/time, random number generation, and data manipulation
import smtplib
import datetime as dt
import random
import pandas

# Read the birthday.csv file into a pandas DataFrame for easy data manipulation
data = pandas.read_csv("birthday.csv")

# Get the current date and time to compare with birthdays in the CSV file
now = dt.datetime.now()
# Extract the month and day from the current date
month = now.month
today = now.day

# Filter the data to find birthdays that match the current month and day
bday = data[(data['month'] == month) & (data['day'] == today)]

# Convert the 'name' column to a list (not actually used in this code)
name = data['name'].tolist()

# Read the contents of the letter.txt files to use as email templates
with open('letter1.txt', 'r') as file:
    letter_1 = file.read()
with open('letter2.txt', 'r') as file:
    letter_2 = file.read()
with open('letter3.txt', 'r') as file:
    letter_3 = file.read()

# Randomly choose a letter to send
random_letter = random.choice((letter_1, letter_2, letter_3))

# Check if there are any matching birthdays
if not bday.empty:
    # If there is a match, get the name of the person
    birthday = bday['name'].values[0]
    # Replace the [NAME] placeholder in the letter with the person's name
    personal_letter = random_letter.replace('[NAME]', birthday)
    # Print the customized letter
    print(personal_letter)

else:
    # If there are no matching birthdays, print a message
    print("No birthdays today")

# Define a function to send an email using SMTP
def send_email(personal_letter):
    # Define the sender's email address and password (App Password generated by Google)
    my_email = "rhyder.sharpe@gmail.com"
    password = "desqcbrcqnjkrxwc"

    # Establish a secure connection to the Gmail SMTP server
    with smtplib.SMTP("smtp.gmail.com") as connection_gmail:
        connection_gmail.starttls()  # Secure connection
        connection_gmail.login(user=my_email, password=password)
        # Send the email with the customized letter
        connection_gmail.sendmail(
            from_addr=my_email,
            to_addrs="rhyder.sharpe@yahoo.com",
            msg=f"Subject:Hello\n\n {personal_letter}"
        )

# Call the send_email function with the customized letter
send_email(personal_letter)
