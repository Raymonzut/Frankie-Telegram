"""A telegram chatbot executing the behavior from the commands module"""


import os

from dotenv import load_dotenv
from telegram.ext import (CommandHandler, MessageHandler, Filters, Updater)

from commands import add_command_handlers
import responses


def __handle_message(update, _context):
    text = str(update.message.text).lower()
    response = responses.sample_responses(text)
    update.message.reply_text(response)


def __error(update, context):
    print(f"Update {update} caused error {context.error}")


def __add_handlers(dispatcher):
    add_command_handlers(lambda c: dispatcher.add_handler(CommandHandler(c['name'], c['action'])))

    dispatcher.add_handler(MessageHandler(Filters.text, __handle_message))
    dispatcher.add_error_handler(__error)

    return dispatcher


def main(api_key):
    """Run a telegram chatbot


       Parameters:
       api_key: for authenticating the bot
    """
    updater = Updater(api_key, use_context=True)
    __add_handlers(updater.dispatcher)

    updater.start_polling(5)
    updater.idle()


if __name__ == '__main__':
    print("Started")
    load_dotenv()
    main(os.getenv('API_KEY'))
