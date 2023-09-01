from pyrogram import Client, filters

# Replace 'YOUR_API_ID' and 'YOUR_API_HASH' with your actual values
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
bot_token = 'YOUR_BOT_TOKEN'

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
