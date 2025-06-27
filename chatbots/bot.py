import discord

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  # Make sure this intent is enabled to read messages content

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if 'hello' in message.content.lower():
        await message.channel.send('Hi there!')
    
    if 'badword' in message.content.lower():
        await message.channel.send("That word isn't allowed!")

    if 'bye' in message.content.lower():
        await message.channel.send("Goodbye! See you later!")

client.run('Discord_Token_Here')
