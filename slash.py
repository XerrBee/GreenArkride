import interactions
import requests
import json
import discord
from env import *

TOKEN = TOKEN_DC
bot = interactions.Client(TOKEN)

@bot.event
async def on_ready():
    print("Ready!")

@bot.command(
name="hello",
description="This is the first command I made!",
scope=874837670520569907,
)

async def hello(ctx: interactions.CommandContext):
    await ctx.send("Hi there!")

url = "https://api.vndb.org/kana/vn"
header = {
    "Content-Type" : "application/json"
}


@bot.command(
    name="vndbsearch",
    description="VNDB API CALL",
    scope=874837670520569907,
    options = [
        interactions.Option(
            name="text",
            description="What you want to say",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ],
)





async def vndbsearch(ctx: interactions.CommandContext,text:str):
    search = {"filters": ["search", "=", text], "fields":"title, image.url, description"}
    x = requests.post(url, headers=header, json=search)
    return_json = x.json()
    image_url =str(return_json['results'][0]['image']['url'])
    title = str(return_json['results'][0]['title'])
    desc = str(return_json['results'][0]['description'])
    # tags = str(return_json['results'][0]['tags'])
    # desc = desc + '\n' + tags
    print(str(return_json['results']))
    embed = interactions.Embed(title=title, description=desc,color = 0xFF5733)
    embed.set_image(url=image_url)
    await ctx.send(embeds=embed)

bot.start()