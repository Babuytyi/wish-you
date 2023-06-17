import telegram
from telegram.ext import Updater, MessageHandler, Filters

# Define token for the Telegram bot
TOKEN = '5832451246:AAH20GMJ0o7QWzXuTltjBOtQbYIdUOQ8bFY'

def echo(update, context):
    message = update.message.text
    update.message.reply_text(message)

def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    
    updater.start_polling()
    print('Bot started')
    updater.idle()

if __name__ == '__main__':
    main()
