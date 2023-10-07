# ----------------------------------------------------------------------------- #
# 1. Obtain the weather information for the hours that are of our interest.
#   - Make a more specific API request that simplifies the information we are
#     getting.
#   * You will have to read the documentation and understand how the API works.
# 2. Use Twilio to send an SMS to our mobile when it's going to rain
#   * As Twilio is not a free to use service, all Twilio code will be commented,
#     you may need to provide your own twilio information in order for the SMS
#     sending service to work.
#   * If you do not feel conformable using twilio, you can use an email service
#     like we have done in previous projects.
# 3. Use PythonAnywhere to automate the script.
#   * You will need to debug some errors between Twilio and PythonAnywhere.
#     https://help.pythonanywhere.com/pages/TwilioBehindTheProxy/

import requests
# from twilio.rest import Client

owm_api_key = "my_openweathermap_key"
owm_api_endpoint = "https://api.openweathermap.org/data/3.0/onecall"

# twilio_acc_sid = "my_twilio_account_id"
# twilio_auth_token = "my_twilio_auth_token"
# twilio_phone_num = "my_twilio_number"
# my_phone_num = "my_phone_num" *VERIFIED ON TWILIO's WEBSITE

my_latitude = 39.469906
my_longitude = -0.376288

# Hour of the day we start checking weather condition (0-24)
hour_to_start_check = 0

# This should be between 0 (No hours check) & 24 (full day check)
num_of_hours_to_check = 12

owm_api_parameters = {
    "lat": my_latitude,
    "lon": my_longitude,
    "appid": owm_api_key,
    "exclude": "current,minutely,daily"
}

owm_api_response = requests.get(owm_api_endpoint, params=owm_api_parameters)
owm_api_response.raise_for_status()

api_response_data = owm_api_response.json()

will_rain = False

if hour_to_start_check + num_of_hours_to_check >= 24:
    print("ERROR: Invalid Daily hours to check parameter.")
    num_of_hours_to_check = 23 - hour_to_start_check

for hour_data in range(hour_to_start_check, hour_to_start_check + num_of_hours_to_check):
    condition_code = api_response_data["hourly"][0]["weather"][hour_data]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella!")
    # client = Client(twilio_acc_sid, twilio_auth_token)
    # message =  client.messages.create(body="Bring an umbrella!", from=twilio_phone_number, to=my_phone_number)
    # print(message.status())

# ----------------------------------------------------------------------------- #
