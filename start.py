from telegram import Update
from telegram.ext import Updater, MessageHandler, CallbackContext
from telegram.ext.filters import Filters

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
BOT_TOKEN = '6286222522:AAGDmZF5xdpakB8_4-SpmATSjerBVG4iohs'

def respond_to_message(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    message = update.message.text
    update.message.reply_text(f"Hi {user.first_name}!\nThis Bot Is No More Working New BOT LInk Is\n\n@MHA_SearchBot")

def main():
    # Create an Updater object with your bot token
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Add a message handler to respond to messages in private chats
    dispatcher.add_handler(MessageHandler(Filters.text, respond_to_message))

    # Start polling for updates from Telegram
    updater.start_polling()
    
    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
