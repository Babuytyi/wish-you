import telegram
from telegram.ext import Updater, MessageHandler, Filters

# Define token for the Telegram bot
TOKEN = '5832451246:AAH20GMJ0o7QWzXuTltjBOtQbYIdUOQ8bFY'

# Define a function to echo back the message
def echo(update, context):
    # Get the message sent by the user
    message = update.message.text
    
    # Echo back the message
    update.message.reply_text(message)

# Define a function to start the bot and listen for messages
def main():
    # Create an Updater instance with the Telegram bot token
    updater = Updater(TOKEN, use_context=True)
    
    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher
    
    # Add a handler to echo back messages
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    
    # Start the bot
    updater.start_polling()
    print('Bot started')

    # Run the bot until pressing Ctrl-C or the process receives SIGINT,SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
