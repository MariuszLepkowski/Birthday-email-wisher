import datetime as dt
import pandas as pd
import smtplib
import os
import random

PLACEHOLDER = "[NAME]"
MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"

today = dt.datetime.today()
today_month = int(today.strftime("%m"))
today_day = int(today.strftime("%d"))

birthdays = pd.read_csv("birthdays.csv")
birthday_month = int(birthdays["month"])
birthday_day = int(birthdays["day"])

receiver_email = birthdays.email

receiver_name = birthdays["name"].to_string(index=False)
random_template = random.choice(os.listdir("letter_templates"))

with open(f"./letter_templates/{random_template}", "r") as file:
    template_contents = file.read()
    template_to_send = template_contents.replace(PLACEHOLDER, receiver_name)

with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS", 587, timeout=120) as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)

    if today_day == birthday_day and today_month == birthday_month:
        connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=receiver_email,
                    msg=f"Subject: Birthday wishes! \n\n{template_to_send}"
        )
