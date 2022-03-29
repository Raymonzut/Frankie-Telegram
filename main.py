import os

from dotenv import load_dotenv
from telegram.ext import *
import Responses as R

print("Started")

def start_command(update, context):
    update.message.reply_text('Type something')

def help_command(update, context):
    update.message.reply_text('If you need help, ask!')

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)
    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main(api_key):
    updater = Updater(api_key, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling(5)
    updater.idle()


if __name__ == '__main__':
    load_dotenv()
    main(os.getenv('API_KEY'))
