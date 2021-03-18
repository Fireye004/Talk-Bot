import discord
import aioconsole

"""
How to Use
    ~~

0- Use the link- https://replit.com/join/cctrktge-fireye to get to this page.

1- Click the big green Button that says 'Run'

2- wait for the console to load. can take anywhere from 5 seconds to 1 minute, so be patient!

3- Enter your name where prompted. 

4- Finally, simply type what you would like to say. The bot will automatically show all incoming messages (across), however can only respond to the most recent one. 
"""



from discord.ext import commands    
client = commands.Bot(command_prefix=".")
client.remove_command('help')

enabled = True
previousGld = ""
User = input("Enter your Name: ")

async def recursion(message):
    global User
    try:
        if message.channel.id != 818556055033348128:
            if message.author == client.user:
                print(f"\nSent- ' {message.content} '\n")
            else:
                print(f"\n\n{message.author}- {message.content}\n")
            res = await aioconsole.ainput('Enter response: ')
            if res == "pass":
                pass
            elif res == "u" or res == "n":
                User = await aioconsole.ainput('Enter your name: ')
                await recursion(message)
            else:
                await message.channel.send(f"{User} says: {res}")
    except RuntimeError:
        pass

@client.event
async def on_ready():
    global User
    if User == "Kai" or User == "Fireye": 
        print(f"Welcome, Supreme Leader {User}")
    else:
        print(f"Welcome, {User}")
    channe = client.get_channel(689926497670135850)
    #await channe.send("Message")
    try:
        res = await aioconsole.ainput('Enter message: ')
        if res == "n":
            pass
        elif res == "u":
            User = await aioconsole.ainput('Enter your name: ')
        else:
            await channe.send(f"{User} says: {res}")
    except RuntimeError:
        pass
    await client.change_presence(activity=discord.Game(name='Howdy!'))
    


@client.command(aliases=["h"])
async def help(ctx):
    embed = discord.Embed(
        title='What is this bot?',
        colour=discord.Colour.orange()
    )
    embed.add_field(name= "Use this bot to communicate with @Fireye#8983 while he is offline", value= "Whenever this bot is online, you can write a message and Fireye will respond through the bot.", inline=False)



@client.command(aliases=["e", "d","disable"])
async def enable(ctx):
    global enable
    if enable == False:
        enable = True
    else:
        enable = False


@client.event
async def on_message(message):
    global User
    try:
        if message.channel.id != 818556055033348128:
            if message.author == client.user:
                print(f"\nSent- '{message.content}'\n")
            else:
                if not message.attatchments:
                    print(f"\n\n{message.author}- {message.content} in {message.channel}\n")
                else:
                    print(f"{User} sent an image: {message.attachment.url}")

            res = await aioconsole.ainput('Enter response: ')
            if res == "pass":
                pass
            elif res == "u" or res == "n":
                User = await aioconsole.ainput('Enter your name: ')
                await recursion(message)
            else:
                await message.channel.send(f"{User} says: {res}")
                #await message.channel.send(f"{res}")
    except RuntimeError:
        pass


client.run("ODIwNTUzMTM5MzA3NDEzNTY0.YE21qQ.LvVtzDwWmnACI2qKEQkKsaXzDJQ")

# oi my dude use the chat 
# did u alt tab or smth
# bro
