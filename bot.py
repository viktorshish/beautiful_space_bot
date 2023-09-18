import argparse
import os
import random
from time import sleep

from dotenv import load_dotenv
import telegram


def get_filename_images():
    with os.scandir('images/') as files:
        name_images = []
        for file in files:
            name_images.append(file.name)

    return name_images


def send_document(file_name, telegram_token, channel_id):
    bot = telegram.Bot(token=telegram_token)
    bot.send_document(
        chat_id=channel_id,
        document=open(f'images/{file_name}', 'rb')
    )


def run_bot(
    image_picture,
    all_images,
    posting_time,
    telegram_token,
    channel_id
):
    four_hour_interval = 14400
    image_names = get_filename_images()

    if image_picture:
        send_document(image_picture, telegram_token, channel_id)

    elif all_images:
        while True:
            for image_name in image_names:
                send_document(image_name, telegram_token, channel_id)
                if not posting_time:
                    sleep(four_hour_interval)
                else:
                    sleep(posting_time)
            random.shuffle(image_names)

    else:
        send_document(random.choice(image_names), telegram_token, channel_id)


def main():
    load_dotenv()

    telegram_token = os.environ['SPACE_TELEGRAM_TOKEN']
    channel_id = os.environ['SPACE_CHANNEL_ID']

    parser = argparse.ArgumentParser(description='Запуск Телеграм Бота')
    parser.add_argument(
        '-a',
        '--all',
        help='Публикация всех скачанных фотографий',
        action='store_true'
    )
    parser.add_argument(
        '-t',
        '--time',
        help='Время частоты публикации фотографий',
        type=int
    )
    parser.add_argument('-n', '--name', help='Имя фотографии')
    args = parser.parse_args()

    run_bot(
        args.name,
        args.all,
        args.time,
        telegram_token,
        channel_id
    )


if __name__ == '__main__':
    main()
