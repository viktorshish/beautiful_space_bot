import datetime
from pathlib import Path
import os
from os.path import splitext
from urllib.parse import urlsplit
from dotenv import load_dotenv

import requests


load_dotenv()


def get_image(image_url, image_number):
    response = requests.get(image_url)
    response.raise_for_status

    image_extension = get_image_extension(image_url)
    Path('images/').mkdir(parents=True, exist_ok=True)
    with open(f'images/spacex{image_number}{image_extension}',
              'wb') as file:
        file.write(response.content)


def get_image_extension(image_url):
    image_path = urlsplit(image_url)[2]
    file_extension = splitext(image_path)[1]

    return file_extension


def fetch_nasa_apod(nasa_apod_url, nasa_api_key, folder_path, image_name):
    params = {
        'api_key': nasa_api_key,
        'count': 5
    }
    response = requests.get(nasa_apod_url, params=params)
    response.raise_for_status()

    nasa_images_url = []
    for image_url in response.json():
        picture_url = image_url.get('hdurl')
        if picture_url:
            nasa_images_url.append(picture_url)

    for image_number, image_url in enumerate(nasa_images_url):
        get_image(image_url, folder_path, image_name, image_number)


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
    nasa_api_key = os.environ['NASA_API_KEY']

    nasa_apod_url = 'https://api.nasa.gov/planetary/apod'
    fetch_nasa_apod(nasa_apod_url, nasa_api_key, 'images/', 'nasa_apod')

    epic_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    fetch_epic(epic_url, nasa_api_key, 'images/', 'nasa_epic', 5)


if __name__ == '__main__':
    main()
