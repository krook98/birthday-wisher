import smtplib
import datetime as dt
import random

MY_EMAIL = {}  # feel free to enter :)
RECIPIENT = {}  # feel free to enter :)
PASSWORD = {}  # feel free to enter :)
today = dt.datetime.now()

if today.weekday() == 1:
    with open('quotes.txt', 'r') as file:
        lines = file.readlines()
        current_quote = random.choice(lines)

    with smtplib.SMTP("smtp.gmail.com", port = 587) as connection:
        connection.starttls()
        connection.login(user = MY_EMAIL, password = PASSWORD)
        connection.sendmail(from_addr = MY_EMAIL,
                            to_addrs = RECIPIENT,
                            msg = f"Subject: Motivation on Monday!\n\n{current_quote}")





