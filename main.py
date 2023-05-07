import datetime as dt
import pandas as pd
import smtplib
import os
import random

MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"
PLACEHOLDER = "[NAME]"

today = dt.datetime.today()
today_month_day = (today.month, today.day)

birthdays = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in birthdays.iterrows()}

if today_month_day in birthdays_dict:
    receiver_email = birthdays_dict[today_month_day]["email"]
    receiver_name = birthdays_dict[today_month_day]["name"]
    random_template = random.choice(os.listdir("letter_templates"))

    with open(f"./letter_templates/{random_template}", "r") as file:
        template_contents = file.read()
        template_to_send = template_contents.replace(PLACEHOLDER, receiver_name)

    with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS", 587, timeout=120) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=receiver_email,
                    msg=f"Subject: Birthday wishes! \n\n{template_to_send}"
        )
