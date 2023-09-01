import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext
from telegram.ext.filters import Filters

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Define your bot token here
TOKEN = '6286222522:AAGDmZF5xdpakB8_4-SpmATSjerBVG4iohs'

# Function to handle the /start command
def start(update: Update, context: CallbackContext):
    user = update.effective_user
    update.message.reply_html(
        f"Hi {user.first_name}!\nThis Bot Is No More Working New BOT Link Is\n\n@MHA_SearchBot"
    )

# Function to handle incoming messages
def echo(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.text)

def main():
    # Create the Updater with your bot's token
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register a command handler for /start
    dp.add_handler(CommandHandler("start", start))

    # Register a message handler to echo messages
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the bot
    updater.start_polling()

    # Run the bot until you send a signal to stop (e.g., Ctrl+C)
    updater.idle()

if __name__ == '__main__':
    main()
