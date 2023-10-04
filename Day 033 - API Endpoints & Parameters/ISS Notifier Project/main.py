# ----------------------------------------------------------------------------- #
import requests
import smtplib
from datetime import datetime

# ---------------------------- CONSTANTS -------------------------------------- #
MY_EMAIL = "test@corderote.com"
MY_PASS = "password12345*"


MY_LAT = 51.587351
MY_LNG = -8.127758
ISS_ANGLE_ERROR = 5.0


# ---------------------------- FUNCTIONS -------------------------------------- #
def is_iss_overhead():
    iss_api_response = requests.get("http://api.open-notify.org/iss-now.json")
    iss_api_response.raise_for_status()
    iss_api_data = iss_api_response.json()

    iss_latitude = float(iss_api_data["iss_position"]["latitude"])
    iss_longitude = float(iss_api_data["iss_position"]["longitude"])

    if (MY_LAT - ISS_ANGLE_ERROR < iss_latitude <= MY_LAT + ISS_ANGLE_ERROR and
            MY_LNG - ISS_ANGLE_ERROR < iss_longitude <= MY_LNG + ISS_ANGLE_ERROR):
        return True

    return False


def is_night():
    api_parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }

    api_response = requests.get("https://api.sunrise-sunset.org/json", params=api_parameters)
    api_response.raise_for_status()

    api_data = api_response.json()

    sunrise_hour = api_data["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset_hour = api_data["results"]["sunset"].split("T")[1].split(":")[0]

    current_time_hour = str(datetime.now().hour)

    if current_time_hour >= sunset_hour or current_time_hour <=sunrise_hour:
        return True

    return False


# ----------------------------------------------------------------------------- #
if is_iss_overhead() and is_night():
    gmail_connection = smtplib.SMTP("smtp.gmail.com")
    gmail_connection.starttls()
    gmail_connection.login(user=MY_EMAIL, password=MY_PASS)

    gmail_connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg="Subject: ISS App Notification.\n\nThe ISS is above you in the sky, go look for it!")

    gmail_connection.close()

# You can put thin inside a while loop with a sleep timer to run the APP in the
# background and get the notification when needed. (If wanted)
# ----------------------------------------------------------------------------- #
