from pathlib import Path
from os.path import splitext

from urllib.parse import urlsplit
import requests


def get_image(image_url, image_name, params=None, image_number=1):
    response = requests.get(image_url, params)
    response.raise_for_status()

    image_extension = get_image_extension(image_url)
    Path('images/').mkdir(parents=True, exist_ok=True)
    with open(f'images/{image_name}{image_number}{image_extension}',
              'wb') as file:
        file.write(response.content)


def get_image_extension(image_url):
    image_path = urlsplit(image_url)[2]
    file_extension = splitext(image_path)[1]

    return file_extension
