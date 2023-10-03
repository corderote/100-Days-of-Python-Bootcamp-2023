# ----------------------------------------------------------------------------- #
import datetime as dt
import pandas
import random
import smtplib

SMTP_CONNECTION = "smtp.gmail.com"
MY_EMAIL = "email@email.com"
MY_PASS = "a12345*"

c_date = dt.datetime.now()
c_month = c_date.month
c_day = c_date.day

bdays_data = pandas.read_csv("./birthdays.csv")
bday_people_month = bdays_data[bdays_data.month == c_month]
bday_people = bday_people_month[bday_people_month.day == c_day]

bday_people = bday_people.to_dict(orient="records")

with smtplib.SMTP(SMTP_CONNECTION) as connection:

    connection.starttls()
    connection.login(MY_EMAIL, MY_PASS)

    for person in bday_people:
        bday_letter_num = random.randint(1, 3)
        with open(f"./letter_templates/letter_{bday_letter_num}.txt") as letter:
            bday_msg = letter.read()
            bday_msg = bday_msg.replace("[NAME]", person["name"])

        msg_subject = f"Happy Birthday {person['name']}!"
        final_msg = f"Subject: {msg_subject}\n\n{bday_msg}"
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=person["email"],
            msg=final_msg
        )

# ----------------------------------------------------------------------------- #
