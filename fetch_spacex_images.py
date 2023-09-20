import argparse

import requests

from get_image import get_image


def fetch_spacex_last_launch(spacex_url, image_name):
    response = requests.get(spacex_url)
    response.raise_for_status()
    image_url = response.json()['links']['flickr']['original']

    for image_number, image_url in enumerate(image_url):
        get_image(image_url, image_name, image_number)


def main():
    parser = argparse.ArgumentParser(
        description='Скачивание фотографий с сайта SpaceX'
    )
    parser.add_argument('-id', '--launch_id', help='ID запуска')
    parser.add_argument('name', help='Имя фотографии')
    args = parser.parse_args()

    spacex_url = f'https://api.spacexdata.com/v5/launches/{args.launch_id}'

    fetch_spacex_last_launch(spacex_url, args.name)


if __name__ == '__main__':
    main()
