# ----------------------------------------------------------------------------- #
# API Keys: Are a way to identify ourselves at the time of accessing an API,
# We can see it as our ID number that we need to use as a parameter to see the
# data from the API.

import requests

# The API with authentication Key that we are going to be using today is from
# https://openweathermap.org/.

# Provided key may be active or not as it was created with the bootcamp test purpose.
# You may need to create an account and provide your own key by changing the
# following variable.
owm_api_key = "my_openweathermap_key"
owm_api_endpoint = "https://api.openweathermap.org/data/3.0/onecall"

my_latitude = 39.469906
my_longitude = -0.376288


owm_api_parameters = {
    "lat": my_latitude,
    "lon": my_longitude,
    "appid": owm_api_key,
}

owm_api_response = requests.get(owm_api_endpoint, params=owm_api_parameters)
owm_api_response.raise_for_status()

api_response_data = owm_api_response.json()
print(api_response_data)
# If you want to check the data and the console seems a bit messy, you can copy
# he output from the print function and paste it in a json file viewer for
# better readability.
# JSON viewer web: https://jsonviewer.stack.hu/

# ----------------------------------------------------------------------------- #
# Environment Variables: When dealing with API Keys and Auth Tokens, we do not
# want to submit that kind of information with the rest of the code, as every
# person running such code should be introducing that variables values or having
# their own ones.
# There is where environment variables come handy, these variables are saved
# locally and can only be acceded from our own system (using the 'os' module)
# In your environment you have to write something like:
# 'export OMW_API_KEY=my_openweathermap_key'
# And to retrieve that variable in your code:
# 'owm_api_key = os.environ.get(OMW_API_KEY)'
# You can always check your environment variables typing 'env' in the console.
# This way we hide our credentials to different APIs or services.

# If you want to check more APIs and do different projects, you can always check:
# https://apilist.fun/
# ----------------------------------------------------------------------------- #
