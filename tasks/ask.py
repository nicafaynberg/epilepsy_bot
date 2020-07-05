from telegram.ext import Updater
from config import TOKEN, USERS
from texts import HELLO_MESSAGE


def main():
    updater = Updater(TOKEN, use_context=True)
    for user in USERS:
        updater.bot.send_message(chat_id=user,
                                 text=HELLO_MESSAGE)


if __name__ == '__main__':
    main()
