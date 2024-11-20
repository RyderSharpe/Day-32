# import smtplib
#
# my_email = "rhyder.sharpe@gmail.com"
# # my_other_email = "rhyder.sharpe@yahoo.com"
# password = "desqcbrcqnjkrxwc"
#
#
# with smtplib.SMTP("smtp.gmail.com") as connection_gmail:
#     # connection_yahoo = smtplib.SMTP("smtp.mail.yahoo.com")
#     connection_gmail.starttls() # Secure connection
#     connection_gmail.login(user=my_email, password=password)
#     connection_gmail.sendmail(
#         from_addr=my_email,
#         to_addrs="rhyder.sharpe@yahoo.com",
#         msg="Subject:Hello\n\nThis is the content of my email. does this even work?"
#     )
#
# # connection_gmail.close()

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
day_of_week = now.weekday()


date_of_birth = dt.datetime(year=1990, month=5, day=5, hour=11, minute=11)
print(date_of_birth)
