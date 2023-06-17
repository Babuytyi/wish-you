import os
import telegram
import datetime
from telegram.ext import CommandHandler, Updater

# Set the Telegram Bot API token as a GitHub Secret
TOKEN = os.environ['TELEGRAM_BOT_TOKEN']

# Create a bot instance
bot = telegram.Bot(TOKEN)

# Define a function to send messages
def send_wishes():
    now = datetime.datetime.now()
    hour = now.hour
    message = ""

    if 6 <= hour < 12:
        message = "Good morning, have a great day ahead!"
    elif 12 <= hour < 18:
        message = "Good afternoon, hope your day is going well!"
    else:
        message = "Good night, sweet dreams!"

    # Send the message to all users
    users = bot.getUpdates()
    for user in users:
        chat_id = user.message.chat_id
        bot.sendMessage(chat_id=chat_id, text=message)

# Define a function to handle user commands
def handle_command(update, context):
    # Parse the command text and convert to lowercase
    text = update.message.text.lower()
    
    # Check if the command is to add a custom wish
    if text.startswith('/addwish'):
        # Extract the wish text from the command
        wish = text.replace('/addwish', '').strip()
        
        # Save the wish to a file or database for future use
        with open('wishes.txt', 'a') as file:
            file.write(wish + '\n')
            
        # Send a confirmation message to the user
        update.message.reply_text("Thanks, I've added your wish to my collection!")
    else:
        # Send a message explaining how to use the bot
        update.message.reply_text("Sorry, I don't recognize that command. To add a custom wish, type /addwish followed by your wish text.")

# Define a function for /start command
def handle_start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to my bot! Type /help to see what I can do.")

# Define a function for /ch command
def handle_check(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm working!")

# Define a function to start the bot and listen for commands
def main():
    # Start the bot
    updater = Updater(TOKEN, use_context=True)
    
    # Register the command handlers
    updater.dispatcher.add_handler(CommandHandler('start', handle_start))
    updater.dispatcher.add_handler(CommandHandler('addwish', handle_command))
    updater.dispatcher.add_handler(CommandHandler('ch', handle_check))

    # Start the bot and listen for updates
    updater.start_polling()
    print("Bot started, listening for commands...")
    updater.idle()

if __name__ == '__main__':
    main()
