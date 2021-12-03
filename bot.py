# bot.py
import os
import ssl
import discord
from dotenv import dotenv_values
import requests
import json
import re
import pyfiglet as pfg

env = dotenv_values('.env')
TOKEN = env['DISCORD_TOKEN']
GUILD = env['DISCORD_GUILD']

client = discord.Client()

quotes_url = "http://api.quotable.io"

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        pfg.figlet_format('Quotes Generator'),
        f'{client.user} is connected to the following server:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    author_regex = r'quote by (.*)'
    author_matches = re.findall(author_regex, message.content)
    keyword_regex = r'keyword:(.*)'
    key_matches = re.findall(keyword_regex, message.content)

    if 'help' in message.content or 'info' in message.content:
        await message.channel.send("""
        This bot uses the quotable API. For more information use the following link: https://opensourcelibs.com/lib/quotable
        
        The bot's functionality includes:
        1) request random quotes 
            (use keyword: 'random quote' in a message statement)
        2) request a random quote by a specific author 
            (any statement with 'quote by <author>')
        3) request 5 random quotes using a keyword 
            (any statement with 'keyword:<keyword>')
        """)

    elif 'random quote' in message.content:
        response = requests.get(f'{quotes_url}/random')

        if response.status_code != 200:
            await message.channel.send('Unable to retrieve a quote from the API')
            return

        data = json.loads(response.text)
        content = data['content']
        author = data['author']
        
        await message.channel.send(f"'{content}' - {author}")

    elif len(author_matches) > 0:
        print('found a match')
        author = author_matches[0]
        print(author)

        response = requests.get(f'{quotes_url}/random?author={author}')

        if response.status_code != 200:
            await message.channel.send("Unable to retrieve author quote from the API. Please use full name of the author. Please note the author may not be in the API's repository")
            return

        data = json.loads(response.text)
        content = data['content']

        await message.channel.send(f"'{content}' - {author}")
    
    elif len(key_matches) > 0:
        print('found a match')
        word = key_matches[0]

        response = requests.get(f'{quotes_url}/search/quotes?query={word}&limit=5&fields=content')

        if response.status_code != 200:
            await message.channel.send('Unable to retrieve a quote from the API')
            return

        data = json.loads(response.text)
        if len(data['results']) == 0:
            await message.channel.send('Nothing found :(')
        for quote in data['results']:
            await message.channel.send(f"'{quote['content']}' - {quote['author']}")
        
    

client.run(TOKEN)
