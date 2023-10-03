# ----------------------------------------------------------------------------- #
# Gmail Setting Steps for the mail app:

# 1. Mail -> Settings -> Security
# 2. Enable two-factor authentication in the mail you are going to be using.
# 3. Once you have 2FA active, look for 'App Passwords'. CLick on it.
# 4. Create a password for 'other type of app', name it, and generate.
# 5. Copy the password and use it for your application.

# Yahoo Setting Steps for the mail app:

# 1. Go to: Your Acc -> Acc Info -> Acc Security -> Log In (again)
# 2. Generate new app password.
# 3. Create a password for 'other type of app', name it, and generate.
# 4. Copy the password and use it for your application.

# ---------------------------- SMTP LIB --------------------------------------- #
import smtplib

gmail_mail = "test@gmail.com"
hotmail_mail = "test@hotmail.com"
yahoo_mail = "test@yahoo.com"

gmail_pass = "password12345*"
hotmail_pass = "password12345*"
yahoo_pass = "password12345*"

# Create the SMTP object that will connect our program. (Like a postman of sorts)
gmail_connection = smtplib.SMTP("smtp.gmail.com")
# hotmail_connection = smtplib.SMTP("smtp.live.com")
# yahoo_connection = smtplib.SMTP("smtp.mail.yahoo.com")

# Enable a security encryption for the email.
gmail_connection.starttls()

# Mail Log in:
gmail_connection.login(user=gmail_mail, password=gmail_pass)

# Send mail:
gmail_connection.sendmail(
    from_addr=gmail_mail,
    to_addrs=hotmail_mail,
    msg="Hello mail!")

# Add a subject to the email:
gmail_connection.sendmail(
    from_addr=gmail_mail,
    to_addrs=hotmail_mail,
    msg="Subject: Hello\n\nThis is the content of the mail.\nHello mail!")

gmail_connection.close()

# You can also use 'with smtplib.SMTP("smtp.gmail.com") as connection:'
# the same way you use files, so the connection is closed once you exit
# the while.

# ----------------------------------------------------------------------------- #
# https://www.pythonanywhere.com/
# Python Everywhere has a free trial that allows us to upload our code and task
# it to make it run every day as we schedule it.
# 1. Sign Up
# 2. Add files (make sure to have everything organized)
# CHECK CODE:
# 3. Go to 'consoles' and create a new bash console.
# 4. Once the console its loaded, type 'python3 main.py'
#    SMTP AUTHENTICATION ERROR: go to the support.google link and follow their steps.
# 5. If no error occurs, you have your code running.
# ACTIVATE IT PERIODICALLY:
# 3. Go to 'tasks'
# 4. Schedule a task by typing 'python3 main.py'
# 5. Check the task log to see how the execution went.
# ----------------------------------------------------------------------------- #
