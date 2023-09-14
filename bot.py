import os

from dotenv import load_dotenv
import telegram


load_dotenv()


def main():
    telegram_token = os.environ['TELEGRAM_TOKEN']

    bot = telegram.Bot(token=telegram_token)

    bot.send_message(chat_id='-1001902360778', text='Hello')
    bot.send_document(
        chat_id='-1001902360778',
        document=open('images/spacex7.gif', 'rb')
    )


if __name__ == '__main__':
    main()
