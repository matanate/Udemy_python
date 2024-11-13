import smtplib
import datetime as dt
import pandas as pd
import random

my_email = "ated@gmail.com"
app_pass = "arascv"

birthdays = pd.read_csv("birthday_wisher\\birthdays.csv")
birthdays_dict = {}
for i in range(0, birthdays.index.size):
    birthdays_dict.setdefault((birthdays["month"][i], birthdays["day"][i]), []).append(
        i
    )

today = dt.datetime.now()
today_month = today.month
today_day = today.day

if (today_month, today_day) in birthdays_dict:
    for i in birthdays_dict[(today_month, today_day)]:
        with open(
            f"birthday_wisher\letter_templates\letter_{random.randint(1,3)}.txt"
        ) as f:
            bd_letter = f.read()
            bd_letter = bd_letter.replace("[NAME]", birthdays["name"][i])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email, app_pass)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=birthdays["email"][i],
                msg=f"Subject:Happy Birthday!\n\n{bd_letter}",
            )
