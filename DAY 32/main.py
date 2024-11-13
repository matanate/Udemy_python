import smtplib
import datetime as dt
import random

my_email = "atedan@gmail.com"
app_pass = "arasqtrucv"


now = dt.datetime.now()
day_of_week = now.weekday()
date_of_birth = dt.datetime(year=1993, month=12, day=22, hour=15, minute=52, second=55)

if day_of_week == 5:
    with open("quotes.txt") as f:
        data = f.readlines()
    rand_quote = random.choice(data)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, app_pass)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Insperation quote\n\n{rand_quote}",
        )
