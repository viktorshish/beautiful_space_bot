import argparse
import datetime
import os

from dotenv import load_dotenv
import requests

from get_image import get_image


def fetch_epic(epic_url, nasa_api_key, picture_name):
    params = {'api_key': nasa_api_key}
    response = requests.get(epic_url, params)
    response.raise_for_status()

    for image_number, image_url in enumerate(response.json()):
        image_date = image_url['date']
        formated_date = datetime.datetime.fromisoformat(image_date)
        format_date = formated_date.strftime('%Y/%m/%d')
        image_name = image_url['image']
        picture_url = f'https://api.nasa.gov/EPIC/archive/natural/{format_date}/png/{image_name}.png'
        get_image(picture_url, picture_name, params, image_number)


def main():
    load_dotenv()

    nasa_api_key = os.environ['NASA_API_KEY']

    parser = argparse.ArgumentParser(
        description='Скачивание фотографий EPIC с сайта NASA'
    )
    parser.add_argument('name', help='Имя фотографии')
    parser.add_argument('-d', '--date', help='Дата в формате YYYY-MM-DD')
    args = parser.parse_args()

    if not args.date:
        epic_url = 'https://api.nasa.gov/EPIC/api/natural'
    else:
        epic_url = f'https://api.nasa.gov/EPIC/api/natural/date/{args.date}'
    fetch_epic(epic_url, nasa_api_key, args.name)


if __name__ == '__main__':
    main()
