import discord
from discord.ext import commands
from bot_mantik import gen_pass
from bot_mantik import emoji_olusturucu 
from bot_mantik import yazi_tura
import os
import random
import requests
print(os.listdir('image_files'))


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık.')

@bot.command()
async def mem(ctx):
    with open(f'image_files/i1.jpg', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_fox_image_url():    
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['image']

def get_pokemon_data(pokemon_name):    
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}'
    res = requests.get(url)
    data = res.json()
    return data['sprites']['front_default']

@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command('dog')
async def dog(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url)

@bot.command('fox')
async def fox(ctx):
    image_url = get_fox_image_url()
    await ctx.send(image_url)

@bot.command('pokemon')
async def pokemon(ctx, pokemon_name):
    image_url = get_pokemon_data(pokemon_name)
    await ctx.send(image_url)

@bot.command(name='merhaba')
async def merhaba(ctx):
    await ctx.send("Selam!")

@bot.command(name='bye')
async def bye(ctx):
    await ctx.send("\U0001f642")

@bot.command(name='pass')
async def generate_pass(ctx):
    await ctx.send(gen_pass(10))

@bot.command(name='yazi_tura')
async def coin_flip(ctx):
    await ctx.send(yazi_tura())

@bot.command(name='emoji')
async def create_emoji(ctx):
    await ctx.send(emoji_olusturucu())

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

bot.run('tokenn')
