from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
BOT_TOKEN = '6384094059:AAFlbEPhnBKsusiUCqMs5BauxAOClAGYi0A'

def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_text(f"Hi {user.first_name}! I'm your bot. How can I help you?")

def main():
    # Create an Updater object with your bot token
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Add a command handler for the /start command
    dispatcher.add_handler(CommandHandler("start", start))

    # Start polling for updates from Telegram
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
