from pyrogram import Client, filters

# Replace 'YOUR_API_ID' and 'YOUR_API_HASH' with your actual values
api_id = '23830477'
api_hash = '19f8365d98fb11c9cd6c1eaa8b1fa4b8'
bot_token = '6286222522:AAGDmZF5xdpakB8_4-SpmATSjerBVG4iohs'

# Create a Pyrogram Client
app = Client('my_bot', api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Define a function to handle incoming messages
@app.on_message(filters.text)
def handle_message(client, message):
    user = message.from_user
    response_message = (
        f"👋 Hi {user.mention()}...!\n"
        "😔 Unfortunately, this bot is no longer in service.\n"
        "Please use the new BOT: @MHA_SearchBot 🚀"
    )
    message.reply_text(response_message)

if __name__ == "__main__":
    # Start the bot
    app.run()
