# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 16:33:33 2024

@author: User
"""

import requests
import pandas as pd

# Step 1: Generate your API KEY from the NASA API portal
# (https://api.nasa.gov/)

# Step 2: Import the requests package and store your API KEY in a variable
API_KEY = 'YOUR_API_KEY'

# Step 3: Explore the 'Astronomy Picture of the Day' (APOD) API endpoint
apod_url = f'https://api.nasa.gov/planetary/apod?api_key={API_KEY}'

# Step 4: Fetch and display the Astronomy Picture of the Day
response = requests.get(apod_url)
apod_data = response.json()

# Display the image
image_url = apod_data['url']
print(f"Astronomy Picture of the Day: {image_url}")

# Step 5: Request the list of Asteroids
asteroids_url = f'https://api.nasa.gov/neo/rest/v1/neo/browse?api_key={API_KEY}'
asteroids_response = requests.get(asteroids_url)
asteroids_data = asteroids_response.json()

# Step 6: Extract relevant information and create a DataFrame
asteroids_list = []
for asteroid in asteroids_data['near_earth_objects']:
    asteroid_id = asteroid['id']
    asteroid_name = asteroid['name']
    min_diameter_km = asteroid['estimated_diameter']['kilometers']['estimated_diameter_min']
    absolute_magnitude = asteroid['absolute_magnitude_h']
    relative_velocity = asteroid['close_approach_data'][0]['relative_velocity']['kilometers_per_second']

    asteroids_list.append({
        'Asteroid ID': asteroid_id,
        'Asteroid Name': asteroid_name,
        'Minimal Estimated Diameter (km)': min_diameter_km,
        'Absolute Magnitude': absolute_magnitude,
        'Relative Velocity (km/s)': relative_velocity
    })

# Step 7: Create a DataFrame
asteroids_df = pd.DataFrame(asteroids_list)

# Step 8: Data pre-processing (if needed)
# (You can perform additional pre-processing tasks here)

# Step 9: Export the DataFrame to a CSV file
asteroids_df.to_csv('asteroids_data.csv', index=False)
print("Data exported to asteroids_data.csv")


 