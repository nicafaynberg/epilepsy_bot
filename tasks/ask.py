from telegram.ext import Updater
from config import PORT, TOKEN, APP_NAME, USERS


def main():
    """Start the bot."""
    updater = Updater(TOKEN, use_context=True)
    # updater.start_webhook(listen="0.0.0.0",
    #                       port=PORT,
    #                       url_path=TOKEN)
    # updater.bot.set_webhook(f"https://{APP_NAME}.herokuapp.com/" + TOKEN)

    for user in USERS:
        updater.bot.send_message(chat_id=user,
                                 text='Приветик')


if __name__ == '__main__':
    main()
