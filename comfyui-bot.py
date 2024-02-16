TOKEN = 'Write your token here'
import discord
from discord.ext import commands
import shutil
from PIL import Image
from discordcomfy import genimg


intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)


# !gen "prompt" in discord
@bot.command(name='gen')
async def _genera(ctx, arg1):
    imgresult = genimg(arg1).save("resultado.png")
    await ctx.send(file=discord.File("resultado.png"))
bot.run(TOKEN)
    
    

