##################### Hard Starting Project ######################
import random
import smtplib
import datetime as dt
import pandas

FILES = ["letter_1.txt","letter_2.txt","letter_3.txt"]
LOGIN = "**********"
APP_PASSWORD = "**********"

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {
    (row['month'], row['day']): row.to_dict() for _, row in data.iterrows()
}

now = dt.datetime.now()
day = now.day
month = now.month

if (month,day) in birthdays_dict:
    selection = random.choice(FILES)
    with open(f"letter_templates/{selection}") as text:
        letter = text.read()
        person_name = birthdays_dict[(month, day)]["name"]
        personalized_letter = letter.replace("[NAME]", person_name)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=LOGIN,password=APP_PASSWORD)
        connection.sendmail(
            from_addr=LOGIN,
            to_addrs= birthdays_dict[(month,day)]["email"],
            msg=f"Subject: Happy Birthday! \n\n{personalized_letter}"
        )

