# ----------------------------------------------------------------------------- #
# API - Application Programming Interface:
# Set of commands functions, protocols and objects that programmers can use to
# create software or interact with an external system.
# https://en.wikipedia.org/wiki/API

# APIs endpoint: Is the location of the external service that we want to
# retrieve the information from. You need to know where the endpoint of the API
# is, so you can use their data. Most of the time is a URL

# API request: Is the action to retrieve the data. Is the teller that allows
# you to exchange information with the data bank.

# API response: When we get the response from the api, is not what we expect
# from them, as it does not contain the json data, but the code that checks how
# the request transaction has completed.


# ----------------------------------------------------------------------------- #
# Requests package requires installation.
import requests
from datetime import datetime

ENDPOINT_URL = "http://api.open-notify.org/iss-now.json"
api_response = requests.get(ENDPOINT_URL)
print(api_response)
# Check the API response in the form of a response code, and we raise an
# exception if an error occurs.
api_response.raise_for_status()
# If we want to hold the data from the API we look for the json inside the response.
api_data = api_response.json()

# ----------------------------------------------------------------------------- #
# International Space Station Current Location:
# http://open-notify.org/Open-Notify-API/ISS-Location-Now/
# http://api.open-notify.org/iss-now.json

# ----------------------------------------------------------------------------- #
# Response codes:
# - 1XX : Hold On
# - 2XX : Everything was successful.
# - 3XX : You do not have permission.
# - 4XX : Something is wrong on your side.
# - 5XX : Something is wrong on the API side.
# More Info: https://www.webfx.com/web-development/glossary/http-status-codes/
# ----------------------------------------------------------------------------- #
# API Parameters:
# Allows us to get specific information from the API, not all APIs have parameters.
# As we have with functions, we can have optional and required parameters.
# The optional ones may have a default value.

# api_response = requests.get("https://api.sunrise-sunset.org/json")
# api_response.raise_for_status()

# If we leave the code like that, the api response will trigger a 404 error,
# as we need to specify the required parameters to our request.

# You can get your latitude and longitude from https://latlong.net.
MY_LAT = 51.587351
MY_LNG = -8.127758

api_parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

api_response = requests.get("https://api.sunrise-sunset.org/json", params=api_parameters)
api_response.raise_for_status()

api_data = api_response.json()

# We take the values that we want from the API and format them as we please by
# using the split python function.
sunrise_hour = api_data["results"]["sunrise"].split("T")[1].split(":")[0]
sunrise_min = api_data["results"]["sunrise"].split("T")[1].split(":")[1]
sunset_hour = api_data["results"]["sunset"].split("T")[1].split(":")[0]
sunset_min = api_data["results"]["sunset"].split("T")[1].split(":")[1]

time_now_hour = str(datetime.now().hour)
time_now_min = str(datetime.now().minute)

print("Sunrise Time: " + sunrise_hour + ":" + sunrise_min)
print("Sunset Time: " + sunset_hour + ":" + sunset_min)
print("Current Time: " + time_now_hour + ":" + time_now_min)

# SAMPLE REQUESTS:
# You can add the parameters to an api string request, to do so, you need to add
# the '?' sign at the end of the api direction, follow it with the parameter name,
# an equal sign '=' and the value of that parameter, if you want to add more than
# one parameter you can add as many as you need separating them using the ampersant
# sign '&'.
# Example: "https://api.sunrise-sunset.org/json?lat=51.587351&lng=-8.127758"

# ----------------------------------------------------------------------------- #
