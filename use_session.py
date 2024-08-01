:from telethon import TelegramClient

# Replace this with your actual session file
session_file = 'your_session_file'  # e.g., 'myaccount.session'

# Initialize the Telegram client with the session file
client = TelegramClient(session_file, api_id=None, api_hash=None)

async def main():
    # Start the client
    await client.start()

    # Fetch your own account details
    me = await client.get_me()
    print(me.stringify())

    # Example: Send a message to yourself
    await client.send_message('me', 'Hello, I am using the session file!')

# Run the script
with client:
    client.loop.run_until_complete(main())
