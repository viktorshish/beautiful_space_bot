import argparse
import os

from dotenv import load_dotenv
import requests

from main import get_image


def fetch_nasa_apod(nasa_apod_url, nasa_api_key, count):
    params = {
        'api_key': nasa_api_key,
        'count': count
    }
    response = requests.get(nasa_apod_url, params=params)
    response.raise_for_status()

    if not count:
        last_image_url = response.json().get('hdurl')
        image_number = 1
        get_image(last_image_url, image_number)
    else:
        nasa_images_url = []
        for image_url in response.json():
            picture_url = image_url.get('hdurl')
            if picture_url:
                nasa_images_url.append(picture_url)

        for image_number, image_url in enumerate(nasa_images_url):
            get_image(image_url, image_number)


def main():
    load_dotenv()

    parser = argparse.ArgumentParser(
        description='Скачивание фотографий APOD с сайта NASA'
    )
    parser.add_argument('-c', '--count',
                        help='Количество скачиваемых фотографий')
    args = parser.parse_args()

    nasa_api_key = os.environ['NASA_API_KEY']
    nasa_apod_url = 'https://api.nasa.gov/planetary/apod'
    
    try:
        fetch_nasa_apod(nasa_apod_url, nasa_api_key, args.count)
    except requests.exceptions.HTTPError:
        exit('Некоректно указано количество скачиваемых фотографий')

if __name__ == '__main__':
    main()
