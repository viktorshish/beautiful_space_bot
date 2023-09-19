import argparse
import datetime
from pathlib import Path
import os

from dotenv import load_dotenv
import requests


def fetch_epic(epic_url, nasa_api_key):
    params = {'api_key': nasa_api_key}
    response = requests.get(epic_url, params)
    response.raise_for_status()

    epic_images_url = []
    for image_url in response.json():
        image_date = image_url['date']
        formated_date = datetime.datetime.fromisoformat(image_date)
        format_date = formated_date.strftime('%Y/%m/%d')
        image_name = image_url['image']
        image_url = f'https://api.nasa.gov/EPIC/archive/natural/{format_date}/png/{image_name}.png'
        epic_images_url.append(image_url)

    for image_number, image_url in enumerate(epic_images_url):
        get_epic_image(nasa_api_key, image_url, image_number)


def get_epic_image(nasa_api_key, image_url, image_number):
    params = {'api_key': nasa_api_key}
    response = requests.get(image_url, params)
    response.raise_for_status

    Path('images').mkdir(parents=True, exist_ok=True)
    with open(f'images/nasa_epic{image_number}.png', 'wb') as file:
        file.write(response.content)


def main():
    load_dotenv()

    nasa_api_key = os.environ['NASA_API_KEY']

    parser = argparse.ArgumentParser(
        description='Скачивание фотографий EPIC с сайта NASA'
    )
    parser.add_argument('-d', '--date', help='Дата в формате YYYY-MM-DD')
    args = parser.parse_args()

    if not args.date:
        epic_url = 'https://api.nasa.gov/EPIC/api/natural'
    else:
        epic_url = f'https://api.nasa.gov/EPIC/api/natural/date/{args.date}'
    fetch_epic(epic_url, nasa_api_key)


if __name__ == '__main__':
    main()
