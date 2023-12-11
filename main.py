import discord
from discord.ext import commands
import os
from webserver import web_server

bot = commands.Bot(command_prefix="-", intents=discord.Intents.all())

try:
  web_server()
  bot.run(os.environ["TOKEN"])
except:
  os.system("kill 1")
