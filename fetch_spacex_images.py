import argparse

import requests

from main import get_image


def fetch_spacex_last_launch(spacex_url):
    response = requests.get(spacex_url)
    response.raise_for_status()
    image_url = response.json()['links']['flickr']['original']

    for image_number, image_url in enumerate(image_url):
        get_image(image_url, image_number)

    return response.json()

def main():
    parser = argparse.ArgumentParser(description='Скачивает фотографии с сайта SpaceX')
    parser.add_argument('-id', '--launch_id', help='ID запуска')
    args = parser.parse_args()

    spacex_url = f'https://api.spacexdata.com/v5/launches/{args.launch_id}'

    try:
        fetch_spacex_last_launch(spacex_url)
    except requests.exceptions.HTTPError as error:
        exit('Фотографий с последнего запуска нет'.format(error))


if __name__ == '__main__':
    main()