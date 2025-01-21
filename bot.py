import discord
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")


def run_discord_bot():
    """
    Runs a Discord bot that listens for messages and responds to them.

    The bot connects to Discord using the provided TOKEN and listens for messages
    in all channels it has access to. If a message starts with a question mark (?),
    the bot will respond to the message in a private message to the user who sent it.
    Otherwise, the bot will respond to the message in the same channel it was sent in.

    Args:
        None

    Returns:
        None
    """
    TOKEN = BOT_TOKEN
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} has connected to Discord!")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        if "https://x.com" in user_message:
            if message.reference:
                replied_message = await message.channel.fetch_message(message.reference.message_id)

                new_content = user_message.replace("https://x.com", "https://fixupx.com")
                await message.delete()  # Delete the user's message
                await replied_message.reply(f"fixTwitter post by `{username}`")
                await message.channel.send(
                    new_content
                )  # Send a new message with updated content
            else:
                new_content = user_message.replace("https://x.com", "https://fixupx.com")
                await message.delete()  # Delete the user's message
                await message.channel.send(f"fixTwitter post by `{username}`")
                await message.channel.send(
                    new_content
                )  # Send a new message with updated content
        elif "https://twitter.com" in user_message:
            if message.reference:
                replied_message = await message.channel.fetch_message(message.reference.message_id)
                
                new_content = user_message.replace("https://twitter.com", "https://fixupx.com")
                await message.delete()  # Delete the user's message
                await replied_message.reply(f"fixTwitter post by `{username}`")
                await message.channel.send(
                    new_content
                )  # Send a new message with updated content
            else:
                new_content = user_message.replace("https://twitter.com", "https://fixupx.com")
                await message.delete()  # Delete the user's message
                await message.channel.send(f"fixTwitter post by `{username}`")
                await message.channel.send(
                    new_content
                )  # Send a new message with updated content
            

    client.run(TOKEN)
