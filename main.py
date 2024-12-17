# main.py

from telethon import TelegramClient, events
import os
import asyncio

# Get API credentials from environment variables
API_ID = int(os.getenv(" 23907675"))
API_HASH = os.getenv("afcbe6fd01e601936137c0fcb11a77aa")
BOT_TOKEN = os.getenv("7626263683:AAEZrt5Y-dLYWJd5jLbeWp4SveAIhvIAdYU")

# Initialize the bot client
bot = TelegramClient('bot', API_ID "20797332", API_HASH"752891ccb9b8b2222554e2757c8b3e9c ").start(bot_token=BOT_TOKEN "7632540110:AAE0HNgDsUqdvAOW4vA_ARixic2XgmBOQzQ")

# In-memory storage for source and destination chats
source_chats = set()
destination_chats = set()
delay_seconds = 0

# Command to start the bot
@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond("Bot started! Use /authorize to log in.")
    raise events.StopPropagation

# Command to log in (authorize) the user
@bot.on(events.NewMessage(pattern='/authorize'))
async def authorize(event):
    await event.respond("Authorization feature goes here.")
    # Add authorization logic as required

# Command to configure source and destination chats
@bot.on(events.NewMessage(pattern='/incoming'))
async def set_source_chat(event):
    chat_id = event.chat_id
    source_chats.add(chat_id)
    await event.respond(f"Source chat added: {chat_id}")

@bot.on(events.NewMessage(pattern='/outgoing'))
async def set_destination_chat(event):
    chat_id = event.chat_id
    destination_chats.add(chat_id)
    await event.respond(f"Destination chat added: {chat_id}")

# Command to start forwarding messages
@bot.on(events.NewMessage(pattern='/work'))
async def start_forwarding(event):
    await event.respond("Started forwarding messages.")

@bot.on(events.NewMessage)
async def forward_messages(event):
    if event.chat_id in source_chats:
        for dest in destination_chats:
            await asyncio.sleep(delay_seconds)  # Delay, if set
            await bot.forward_messages(dest, event.message)

# Additional commands for transforming text, filtering, etc.
# Example: Command to set delay
@bot.on(events.NewMessage(pattern='/delay'))
async def set_delay(event):
    global delay_seconds
    delay_seconds = int(event.message.text.split(' ', 1)[1])
    await event.respond(f"Delay set to {delay_seconds} seconds.")

# Run the bot
print("Bot is running...")
bot.run_until_disconnected()
