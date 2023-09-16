import argparse
import os
import random
from time import sleep

from dotenv import load_dotenv
import telegram


load_dotenv()


def get_filename_images():
    with os.scandir('images/') as files:
        name_images = []
        for file in files:
            name_images.append(file.name)

    return name_images


def run_bot(args):
    interval_time_in_seconds = 14400
    name_images = get_filename_images()

    telegram_token = os.environ['TELEGRAM_TOKEN']
    channel_id = os.environ['CHANNEL_ID']
    bot = telegram.Bot(token=telegram_token)

    if args.name:
        bot.send_document(
                chat_id=channel_id,
                document=open(f'images/{args.name}', 'rb')
        )
    elif args.all:
        while True:
            for name_image in name_images:
                bot.send_document(
                    chat_id=channel_id,
                     document=open(f'images/{name_image}', 'rb')
                )
            if not args.time:
                sleep(interval_time_in_seconds)
            else:
                sleep(int(args.time))
            random.shuffle(name_images)
    else:
        bot.send_document(
                chat_id=channel_id,
                document=open(f'images/{random.choice(name_images)}', 'rb')
        )


def main():
    parser = argparse.ArgumentParser(description='Запуск Телеграм Бота')
    parser.add_argument('-a', '--all', help='Публикация всех скачанных фотографий')
    parser.add_argument('-t', '--time', help='Время частоты публикации фотографий')
    parser.add_argument('-n', '--name', help='Имя фотографии')
    args = parser.parse_args()

    run_bot(args)


if __name__ == '__main__':
    main()
