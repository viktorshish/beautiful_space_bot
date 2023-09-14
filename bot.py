import os

from dotenv import load_dotenv
import telegram


load_dotenv()


if __name__ == '__main__':
    telegram_token = os.environ['TELEGRAM_TOKEN']
    bot = telegram.Bot(token=telegram_token)

    updates = bot.get_updates()

    bot.send_message(chat_id='@test_grous', text='Hello')
