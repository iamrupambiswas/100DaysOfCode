import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Twilio and API credentials stored in environment variables
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

API_KEY = os.getenv("WEATHER_API_KEY")
MY_LAT = 12.971599
MY_LONG = 77.594566

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt": 4
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_list = response.json()["list"]
will_rain = False

for res in weather_list:
    condition_code = res["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    message = client.messages.create(
        body="It's going to rain today! Don't forget to bring ☂️",
        from_=os.getenv("TWILIO_PHONE_NUMBER"),
        to=os.getenv("MY_PHONE_NUMBER")
    )
    print(message.status)
else:
    message = client.messages.create(
        body="It's not going to rain today!",
        from_=os.getenv("TWILIO_PHONE_NUMBER"),
        to=os.getenv("MY_PHONE_NUMBER")
    )
    print(message.status)
