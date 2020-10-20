import yaml
import discord
# import asyncio
import random

with open("./config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.BaseLoader)

TOKEN = cfg['bot_token']
GUILD = cfg['guild']

client = discord.Client()


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    mirror_mirror = ['you\'re fucking handsome', 'wow, gorgeous', 'i can\'t believe it, stunning']
    brooklyn_99_quotes = ['I\'m the human form of the 💯 emoji.',
                          'Bingpot!',
                          (
                              'Cool. Cool cool cool cool cool cool cool, '
                              'no doubt no doubt no doubt no doubt.'
                          )
                          ]
    print('message.content', message.content)
    print(message.author, message)
    # print('message.channel.id', message.channel.id)
    if message.content == 'mirror mirror on the wall.':
        if message.author.name == 'lukeOida':
            response = 'fucking ewww bro'
            await message.channel.send(response)
        else:
            response = random.choice(mirror_mirror)
            await message.channel.send(response)

    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)
        await message.delete()


    if message.content == 'Let’s overthrow the lukian dictatorship!!!!':
        response = 'One does not establish a dictatorship in order to safeguard a revolution; one makes the revolution in order to establish the dictatorship. -Orwell, 1984'
        await message.channel.send(response)
        await message.delete()


    if message.content == 'no homo':
        response = 'just this once!'
        await message.channel.send(response)
    # if message.channel.id == 766700249501794314:
    #    response = ''.join(x.upper() if random.randint(0, 1) else x for x in message.content) + ' maybe this was a bad idea...'
    # response = ''.join(x.upper() if random.randint(0, 1) else x for x in arguments)
    #   await message.channel.send(response)


client.run(TOKEN)
