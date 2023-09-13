import os

from dotenv import load_dotenv
import requests

from main import get_image, get_image_extension


def fetch_nasa_apod(nasa_apod_url, nasa_api_key):
    params = {
        'api_key': nasa_api_key,
        'count': 2
    }
    response = requests.get(nasa_apod_url, params=params)
    response.raise_for_status()

    nasa_images_url = []
    for image_url in response.json():
        picture_url = image_url.get('hdurl')

        if picture_url:
            nasa_images_url.append(picture_url)

    for image_number, image_url in enumerate(nasa_images_url):
        get_image(image_url, image_number)


def main():
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    nasa_apod_url = 'https://api.nasa.gov/planetary/apod'
    fetch_nasa_apod(nasa_apod_url, nasa_api_key)


if __name__ == '__main__':
    main()