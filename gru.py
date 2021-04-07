import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(intents=intents, command_prefix=']')
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(msg):
    if 'girl' in msg.content:
        channel = msg.channel
        author = msg.author
        await msg.delete()
        pog = msg.content
        sent = pog.replace("girl", "gorl")
        await channel.send(f"{author.mention} - " + sent)
    if "Girl" in msg.content:
        channel = msg.channel
        author = msg.author
        await msg.delete()
        pog = msg.content
        sent = pog.replace("Girl", "Gorl")
        await channel.send(f"{author.mention} - " + sent)
    if "gru" in msg.content:
        channel = msg.channel
        author = msg.author
        await channel.send(f"{author.mention} - That is *Gru* to you, disrespectful...")
    await bot.process_commands(msg)

   
@bot.command()
async def say(ctx, *, message):
    await ctx.message.delete()
    await ctx.send(message)

@bot.command()
async def secretcoms(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="GruBot Secret Commands!", description="Don't tell lol")
    embed.add_field(name="Wren", value="Returns faggot")
    embed.add_field(name="Sex", value="Gru sexes you :weary")
    embed.add_field(name="Akins", value="My daddy ;)")
    embed.add_field(name="DuckBot", value="Gay")
    embed.add_field(name="Source", value="Displays the source code, for my sexy devs out there")
    embed.add_field(name="Github", value="Send a link to the bots github repo")
    await ctx.message.author.send(embed=embed)

@bot.command()
async def embed(ctx, title, description, name, value):
    embed = discord.Embed(title=title, description=description)
    embed.add_field(name=name, value=value)
    await ctx.send(embed=embed)
    
@bot.command()
async def credits(ctx):
    embed = discord.Embed(title="GruBot V.1", description="A sexy bot of our lord and saviour Gru :weary:")
    embed.add_field(name="Contributors", value="-")
    embed.add_field(name="Akins", value="-")
    embed.add_field(name="Stack Overflow", value="...")
    embed.set_image(url='https://i.redd.it/qm042clcd7g41.jpg')
    await ctx.send(embed=embed)

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="GruBot V.1", description="Made by Akins")
    embed.add_field(name="Help", value="Displays this command")
    embed.add_field(name="Ping", value="Checks if the bot is online")
    embed.add_field(name="Embed", value="Makes a cool embedded message")
    embed.add_field(name="Say", value="Makes the bot say a certain word or phrase")
    embed.add_field(name="Credits", value="Displays the bots credits")
    embed.set_footer(text="GruBot's main purpose is to replace every instance of *g*irl, with gorl, to satisfy our lord and saviour Gru.")
    await ctx.send(embed=embed)
    
@bot.command()
async def ping(ctx):
    await ctx.send("pong")

@bot.command()
async def wren(ctx):
    await ctx.message.delete()
    await ctx.message.author.send("What a Faggot amiright?")

@bot.command()
async def sex(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="Gru touches your nono area UwU...")
    embed.set_image(url='https://cdn140.picsart.com/306455722075201.jpg?type=webp&to=min&r=640')
    await ctx.message.author.send(embed=embed)
    
@bot.command()
async def akins(ctx):
    await ctx.message.delete()
    await ctx.send("Akins is hot lol")
    
@bot.command()
async def duckbot(ctx):
    await ctx.message.delete()
    await ctx.send("DuckBot is gay, so is Akins")
    
@bot.command()
async def source(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="Source Code", url='https://replit.com/join/tacbunfb-pewdrip')
    await ctx.message.author.send(embed=embed)

@bot.command()
async def github(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="GruBot Github Repo", url='https://github.com/Vigilantly-2328/grubot')
    await ctx.message.author.send(embed=embed)
    
bot.run(token)
