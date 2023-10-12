# ----------------------------------------------------------------------------- #
# HTTPS Requests:
# GET: Ask an external system for a particular piece of information (data) and
#      they give that to us as a response.
# POST: We are the ones that give the data to the external system. The only thing
#       that interest us from the response is if everything went successfully.
# PUT: Is when you update a piece of data, so you have something already in your
#      external system, and you want to modify it.
# DELETE: Is when you want to delete a piece of data from the external system.

# Today we are going to be building our habit tracker using the pixela API by
# posting our habits tracking data.
# URL: pixel.la

import requests
import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_USER_TOKEN = "my_pixela_user_token"
PIXELA_USERNAME = "my_pixela_username"
PIXELA_GRAPH_ID = "my_pixela_graph_id"

# USER CREATION.
pixela_user_params = {
    "token": PIXELA_USER_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# When using a post request, our params are send inside a json variable.
pixela_response = requests.post(url=PIXELA_ENDPOINT, json=pixela_user_params)
print(pixela_response.text)

# GRAPH CREATION.
pixela_graph_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs"

pixela_graph_params = {
    "id": PIXELA_GRAPH_ID,
    "name": "Coding Habit Graph",
    "unit": "hours",
    "type": "float",
    "color": "momiji",
}

pixela_headers = {
    "X-USER-TOKEN": PIXELA_USER_TOKEN,
}

# pixela_response = requests.post(url=pixela_graph_endpoint, json=pixela_graph_params, headers=pixela_headers)
# print(pixela_response.text)

# POSTING A PIXEL TO OUR GRAPH.
pixela_pixel_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH_ID}"

# We can use the 'daytime.strftime()' method to automate the date param for our graph.
current_date = datetime.datetime.now()
pixela_date = current_date.strftime("%Y%m%d")

pixela_pixel_params = {
    "date": pixela_date,
    "quantity": "1.5"
}

# pixela_response = requests.post(url=pixela_pixel_endpoint, json=pixela_pixel_params, headers=pixela_headers)
# print(pixela_response.text)

# UPDATE A PIXEL
pixela_update_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH_ID}/{pixela_date}"

pixela_update_params = {
    "quantity": "2.5"
}

# pixela_response = requests.put(url=pixela_update_endpoint, json=pixela_update_params, headers=pixela_headers)
# print(pixela_response.text)

# DELETE A PIXEL:
pixela_delete_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH_ID}/{pixela_date}"
# pixela_response = requests.put(url=pixela_delete_endpoint, headers=pixela_headers)
# print(pixela_response.text)

# ----------------------------------------------------------------------------- #
