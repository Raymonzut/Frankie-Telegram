import os

from dotenv import load_dotenv
from telegram.ext import *

from Commands import add_command_handlers
import Responses


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = Responses.sample_responses(text)
    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def add_handlers(dispatcher):
    add_command_handlers(lambda c: dispatcher.add_handler(CommandHandler(c['name'], c['action'])))

    dispatcher.add_handler(MessageHandler(Filters.text, handle_message))
    dispatcher.add_error_handler(error)

    return dispatcher


def main(api_key):
    updater = Updater(api_key, use_context=True)
    add_handlers(updater.dispatcher)

    updater.start_polling(5)
    updater.idle()


if __name__ == '__main__':
    print("Started")
    load_dotenv()
    main(os.getenv('API_KEY'))
