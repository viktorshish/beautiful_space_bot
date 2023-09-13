import datetime
from pathlib import Path
import os

from dotenv import load_dotenv
import requests


def fetch_epic(epic_url, nasa_api_key, folder_path, image_name, count_images):
    params = {'api_key': nasa_api_key}
    response = requests.get(epic_url, params)

    epic_images_url = []
    for image_url in response.json():
        image_date = image_url['date']
        formated_date = datetime.datetime.fromisoformat(image_date)
        format_date = formated_date.strftime('%Y/%m/%d')
        image_name = image_url['image']
        image_url = f'https://api.nasa.gov/EPIC/archive/natural/{format_date}/png/{image_name}.png'
        epic_images_url.append(image_url)

    for image_number, image_url in enumerate(epic_images_url[:count_images]):
        get_epic_image(nasa_api_key, image_url, folder_path,
                       image_name, image_number)


def get_epic_image(nasa_api_key, image_url, folder_path,
                   image_name, image_number):
    params = {'api_key': nasa_api_key}
    response = requests.get(image_url, params)
    response.raise_for_status

    Path(folder_path).mkdir(parents=True, exist_ok=True)
    with open(f'{folder_path}{image_name}{image_number}.png',
              'wb') as file:
        file.write(response.content)


def main():
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']

    epic_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    fetch_epic(epic_url, nasa_api_key, 'images/', 'nasa_epic', 5)


if __name__ == '__main__':
    main()
