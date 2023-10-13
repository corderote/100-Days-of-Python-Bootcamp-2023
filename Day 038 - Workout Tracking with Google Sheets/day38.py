# ----------------------------------------------------------------------------- #
import requests
import datetime

NUTRITIONIX_APP_ID = "nutrionix_app_id"
NUTRITIONIX_API_KEY = "nutrionix_app_key"

SHEETY_USERNAME = "sheety_username"
SHEETY_PASSWORD = "sheety_password"
SHEETY_TOKEN = "sheety_auth_tocken"

NUTRITIONIX_API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = "sheety_project_endpoint"

USER_GENDER = "male"
USER_WEIGHT_KG = 60.0
USER_HEIGHT_CM = 173.0
USER_AGE = 28

current_date = datetime.datetime.now()

user_input_exercise = input("Tell me about the exercises you have been doing today: ")

nutritionix_headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}

nutritionix_params = {
    "query": user_input_exercise,
    "gender": USER_GENDER,
    "weight_kg": USER_WEIGHT_KG,
    "height_cm": USER_HEIGHT_CM,
    "age": USER_AGE,
}

nutritionix_data = requests.post(url=NUTRITIONIX_API_ENDPOINT, json=nutritionix_params, headers=nutritionix_headers)
nutritionix_data.raise_for_status()
nutritionix_data = nutritionix_data.json()

today_date = current_date.strftime("%d/%m/%Y")
current_time = current_date.strftime("%X")

for exercise in nutritionix_data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # Bearer Token Authentication
    bearer_headers = {
        "Authorization": SHEETY_TOKEN
    }

    # You may add the header or the auth (auth=(SHEET_USERNAME, SHEET_PASSWORD))
    # to add the authority of the changes for the Google sheet document.
    sheet_response = requests.post(SHEET_ENDPOINT, json=sheet_inputs)

    print(sheet_response.text)
# ----------------------------------------------------------------------------- #
