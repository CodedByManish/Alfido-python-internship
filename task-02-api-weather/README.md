# Task 2 - API Integration & JSON Handling

## Overview

This project demonstrates how to fetch and process real-time weather data using the OpenWeather API. It focuses on API integration, JSON parsing, and basic error handling using Python.

## Features

* Fetch weather data by city name
* Parse JSON response from API
* Display temperature, humidity, weather condition, and wind speed
* Handle common API and network errors

## Technologies Used

* Python 3
* Requests library
* OpenWeather API
* JSON handling

## Setup Instructions

1. Create and activate a virtual environment:

   ```
   Windows :                               macOS/Linux :
   
   python -m venv venv                    python3 -m venv venv
   venv\Scripts\activate                  source venv/bin/activate
   ```

2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file:

   ```
   OPENWEATHER_API_KEY=your_api_key_here
   ```

4. Run the application:

   ```
   python app.py
   ```

## Example Output

```
Enter city name: Kathmandu

Result:
{
  "city": "Kathmandu",
  "temperature": 22,
  "humidity": 60,
  "weather": "clear sky",
  "wind_speed": 3.2
}
```

## Outcome

* API requests in Python
* Working with JSON data
* Handling errors in real-world API calls
* Basic backend scripting practice
