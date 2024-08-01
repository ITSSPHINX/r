from telethon import TelegramClient

# Replace these with your actual session file, API ID, and API hash
session_file = '+98 9378543697.session'  # Your session file
api_id = 26159648                       # Your API ID
api_hash = '4ab1fd7ab6a2e35d629f31992d5839fe'  # Your API hash

# Initialize the Telegram client with the session file
client = TelegramClient(session_file, api_id, api_hash)

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
