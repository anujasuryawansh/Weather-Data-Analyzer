import requests
import sqlite3
from datetime import datetime

API_KEY = 'aad648111638be9b56452a4f63554964' 
LAT = '18.516726'
LONG = '73.856255'
url = f'https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LONG}&appid={API_KEY}&units=metric'

# SQLite database configuration
DB_NAME = 'C:\\Users\\bhosa\\Desktop\\weatherapi\\weather_data.db'

# Function to fetch weather data from OpenWeatherMap API
def fetch_weather_data():
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = {
                'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed']
            }
            return weather
        else:
            print(f"Error: Unable to fetch data. Status Code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

# Function to create SQLite DB and table if it doesn't exist
def create_db_and_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS weather (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        date TEXT,
                        temperature REAL,
                        humidity REAL,
                        wind_speed REAL
                      )''')
    conn.commit()
    conn.close()

# Function to store fetched weather data into SQLite DB
def store_weather_data(weather):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO weather (date, temperature, humidity, wind_speed)
                      VALUES (?, ?, ?, ?)''', 
                      (weather['date'], weather['temperature'], weather['humidity'], weather['wind_speed']))
    conn.commit()
    conn.close()
    print("Weather data stored in database.")

# Main function to fetch and store weather data
def main():
    create_db_and_table()  # Create DB and table if not present
    weather = fetch_weather_data()  # Fetch weather data
    if weather:
        store_weather_data(weather)  # Store data in DB

if __name__ == '__main__':
    main()