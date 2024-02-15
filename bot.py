import discord
import responses
from discord import commands
import interactions
from env import *


async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = TOKEN_DC
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    

    # @bot.command(description="Sends the bot's latency.") # this decorator makes a slash command
    # async def ping(ctx): # a slash command will be created with the name "ping"
    #     await ctx.respond(f"Pong! Latency is {bot.latency}")


    with open('Badwords.txt', 'r') as f:
        words = f.read()
        banned_words = words.split()
    
    with open('InterestedWords.txt', 'r') as f:
        words = f.read()
        interested_words = words.split()
    
    # @client.slash_command()
    # async def lol(ctx: discord.ApplicationContext):
    #     await ctx.response.send_message("LOL")
    
    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
    
    async def checkMessages(message, value_list):
        for word in value_list:
            if word in message.content.lower() or word in message.content.upper():
                user = await client.fetch_user(message.author.id)
                print(message.author.id)
                await message.delete()
                await message.channel.send(f"{message.author.mention} You cannot say that word!")
                await user.send("Don't send that message!")


    @client.event
    async def on_message(message):
        await checkMessages(message, banned_words)
        for word in interested_words:
            if word in message.content.lower() or word in message.content.upper():
                user = await client.fetch_user(325556290694938634)
                await user.send("Someone mentioned: " + word)

        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said '{user_message}'({channel})")

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)
        
    
    client.run(TOKEN)