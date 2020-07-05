import os
import logging
from telegram.ext import Updater

from dotenv import load_dotenv

from dialuge_structure import conversation

load_dotenv()

TOKEN = os.getenv("TOKEN")
APP_NAME = os.getenv("APP_NAME")
PORT = int(os.environ.get('PORT', '8443'))

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)
    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=TOKEN)
    updater.bot.set_webhook(f"https://{APP_NAME}.herokuapp.com/" + TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    dp.add_handler(conversation)
    dp.add_error_handler(error)
    updater.idle()


if __name__ == '__main__':
    main()
