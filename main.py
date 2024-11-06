import smtplib

my_email = "rhyder.sharpe@gmail.com"
# my_other_email = "rhyder.sharpe@yahoo.com"
password = "desqcbrcqnjkrxwc"


with smtplib.SMTP("smtp.gmail.com") as connection_gmail:
    # connection_yahoo = smtplib.SMTP("smtp.mail.yahoo.com")
    connection_gmail.starttls() # Secure connection
    connection_gmail.login(user=my_email, password=password)
    connection_gmail.sendmail(
        from_addr=my_email,
        to_addrs="rhyder.sharpe@yahoo.com",
        msg="Subject:Hello\n\nThis is the content of my email"
    )


# connection_gmail.close()
