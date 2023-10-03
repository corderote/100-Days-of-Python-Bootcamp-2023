# ---------------------------- MOTIVATIONAL MONDAY MAIL ----------------------- #
import datetime as dt
import smtplib
import random

mail = "test@gmail.com"
m_pass = "password12345*"

current_dt = dt.datetime.now()
current_weekday = current_dt.weekday()

if current_weekday == 0:

    msg_subject = f"Happy Monday {current_dt.date()}"

    with open("quotes.txt", ) as quotes_file:
        # quotes_file.readlines() also gives us the list we are looking for.
        quotes_data = quotes_file.read()
        quotes_list = quotes_data.split("\n")
        quote_msg = random.choice(quotes_list)

    final_msg = f"Subject: {msg_subject}\n\n{quote_msg}"
    print(final_msg)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(mail, m_pass)
        connection.sendmail(
            from_addr=mail,
            to_addrs=mail,
            msg=msg_subject
        )

# ----------------------------------------------------------------------------- #
