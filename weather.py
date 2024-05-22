import requests
import json

#Add your API Key
api_key = ""

base_url = "https://api.openweathermap.org/data/2.5/weather?"

def get_weather(city):
    url = f"{base_url}q={city}&appid={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = json.loads(response.text)
        temperature = data["main"]["temp"] - 273.15
        wind_speed = data["wind"]["speed"]
        humidity = data["main"]["humidity"]
        rain_chance = 0 
        if "rain" in data:
            rain_chance = data["rain"]["1h"]
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON response: {e}")
    else:
        print(f"City: {city}")
        print(f"Temperature: {temperature:.2f} °C")
        print(f"Wind Speed: {wind_speed:.2f} m/s")
        print(f"Humidity: {humidity}%")
        if rain_chance > 0:
            print(f"Rain: {rain_chance} mm (past hour)")
        else:
            print("No rain data available")

city = input("Enter city name: ")

get_weather(city)
