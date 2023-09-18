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


def send_document(file_name):
    telegram_token = os.environ['TELEGRAM_TOKEN']
    channel_id = os.environ['CHANNEL_ID']
    bot = telegram.Bot(token=telegram_token)
    bot.send_document(
        chat_id=channel_id,
        document=open(f'images/{file_name}', 'rb')
    )


def run_bot(args):
    four_hour_interval = 14400
    image_names = get_filename_images()

    if args.name:
        send_document(args.name)

    elif args.all:
        while True:
            for image_name in image_names:
                send_document(image_name)
                if not args.time:
                    sleep(four_hour_interval)
                else:
                    sleep(args.time)
            random.shuffle(image_names)

    else:
        send_document(random.choice(image_names))


def main():
    load_dotenv()

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

    run_bot(args)


if __name__ == '__main__':
    main()
