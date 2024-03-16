import requests  # Import the requests library for making HTTP requests

def get_weather(city, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather?"  # Base URL for the OpenWeatherMap API
    params = {
        "q": city,  # Specify the city for which weather data is requested
        "appid": api_key,  # Provide your OpenWeatherMap API key
        "units": "metric"  # Specify the units for temperature (metric for Celsius, imperial for Fahrenheit)
    }
    response = requests.get(base_url, params=params)  # Send a GET request to the API with the specified parameters
    if response.status_code == 200:  # Check if the request was successful (status code 200)
        weather_data = response.json()  # Convert the JSON response to a Python dictionary
        return weather_data  # Return the weather data as a dictionary
    else:
        print("Error fetching weather data.")  # Print an error message if fetching data fails
        return None  # Return None if there was an error

# Replace 'your_api_key' with your actual OpenWeatherMap API key
api_key = 'cf128e77a45e377b15e48a80dd4f67ba'
city_name = 'London'  # Replace with the city you want to get weather data for

weather_info = get_weather(city_name, api_key)  # Call the get_weather function to fetch weather data
if weather_info:  # Check if weather_info is not None (i.e., data was fetched successfully)
    print(f"Weather in {city_name}:")
    print(f"Temperature: {weather_info['main']['temp']}°C")  # Print temperature in Celsius
    print(f"Description: {weather_info['weather'][0]['description']}")  # Print weather description
    print(f"Humidity: {weather_info['main']['humidity']}%")  # Print humidity percentage
else:
    print("Failed to fetch weather data.")  # Print a failure message if fetching data fails
