import discord
from discord.ext import commands
import bang

cogs = [bang]

client = commands.Bot(command_prefix='?', intents=discord.Intents.all())


@client.event
async def on_ready():
    print("Bot is ready")


for i in range(len(cogs)):
    cogs[i].setup(client)


client.run("Bot Token")
