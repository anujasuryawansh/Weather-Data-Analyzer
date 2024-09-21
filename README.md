# Weather-Data-Analyzer

## Overview
This Python application fetches weather data from a public API, stores it in a local SQLite database, and provides analysis and visualization of weather trends over time.

## Features
- Fetches weather data (temperature, humidity, wind speed) at regular intervals.
- Stores data in an SQLite database.
- Provides basic statistical analysis of weather data.
- Visualizes trends using Matplotlib.

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.6 or higher
- pip (Python package installer)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/weather-data-aggregator.git
   cd weather-data-aggregator

2.Install the required packages:
   pip install requests ,numpy ,pandas ,matplotlib ,seaborn

3. Set up your environment:

You will need an API key from a public weather API (e.g., OpenWeatherMap). Sign up and get your API key.
Configure the API key:

4.Open the weather.py file and update the API_KEY variable with your actual API key

## Usage
1.Run the application:

2.bash
Copy code
python weather.py

3.Fetch data:

The application will fetch weather data for the specified location at regular intervals (e.g., every hour) and store it in weather_data.db.
Analyze data:

Use the provided functions in analysis.py to perform statistical analysis on the stored data.

4.Visualize data:

Run the visualization script to generate plots for temperature, humidity, and wind speed trends:

## Output
The application will generate plots that show the trends in temperature and humidity over time.
Basic statistical analysis results (e.g., average temperature, average humidity) will be printed to the console.
