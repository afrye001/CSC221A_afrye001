# Program to retrieve the APOD (Astrology Picture of the Day) from the NASA website using their API.  

import requests
import os
from datetime import datetime, timedelta

def get_apod_images(start_date, end_date):
    api_url = "https://api.nasa.gov/planetary/apod"
    api_key = "gKlBTUAU3ZOv3THCi0CXMc25nbN2zsioyex93JaL" 

    os.makedirs("apod_images", exist_ok=True)

    current_date = start_date
    while current_date <= end_date:
        date_str = current_date.strftime("%Y-%m-%d")
        params = {"date": date_str, "api_key": api_key}

        response = requests.get(api_url, params=params)
        if response.status_code == 200:
            data = response.json()
            image_url = data["url"]
            image_title = data["title"]
            image_description = data["explanation"]

            image_response = requests.get(image_url)
            if image_response.status_code == 200:
                image_filename = f"apod_images/{date_str}.jpg"
                with open(image_filename, "wb") as f:
                    f.write(image_response.content)
                print(f"Downloaded {image_title} ({date_str})")
            else:
                print(f"Failed to download {image_title} ({date_str})")

        else:
            print(f"Failed to retrieve data for {date_str}")

        current_date += timedelta(days=1)

if __name__ == "__main__":
    start_date = datetime(2024, 5, 1)  
    end_date = datetime(2024, 5, 5)    
    get_apod_images(start_date, end_date)
