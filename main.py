import discord
from discord.ext import commands
import asyncio

initial_extensions = ['cogs.moderation', 'cogs.fun', 'cogs.music']

intents = discord.Intents.all()
bot = commands.Bot(intents=intents, command_prefix=']')
bot.remove_command('help')

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}, ID: {bot.user.id}")
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game("GruBot - prefix = ]"))

@bot.event
async def on_message(msg):
    if 'girl' in msg.content:
        channel = msg.channel
        author = msg.author
        pog = msg.content
        message = pog.replace('girl', 'gorl')
        await msg.delete()
        await channel.send(f"{author.mention} - {message}")
    if 'Girl' in msg.content:
        channel = msg.channel
        author = msg.author
        pog = msg.content
        message = pog.replace('Girl', 'Gorl')
        await msg.delete()
        await channel.send(f"{author.mention} - {message}")
    if 'gru' in msg.content:
        channel = msg.channel
        author = msg.author
        pog = msg.content
        message = pog.replace('gru', 'Gru*')
        await msg.delete()
        await channel.send(f"{author.mention} - {message}")

@bot.group(invoke_without_command=True)
async def help(ctx):
        embed=discord.Embed(title="GruBot 3.0.0 Help Command", url="https://discord.com/oauth2/authorize?client_id=829110030736949298&scope=bot&permissions=8", description="The help command for GruBot V.2")
        embed.set_author(name="Akins", icon_url="https://cdn.discordapp.com/avatars/707643377621008447/8e56c7abb270316601cc1fc0f9c8c06a.png?size=1024")
        embed.add_field(name="Help", value="Displays this command", inline=False)
        embed.add_field(name="Moderation", value="Displays the moderation help page", inline=False)
        embed.add_field(name="Music", value="Displays the music help page", inline=False)
        embed.add_field(name="Fun", value="Displays the fun help page", inline=False)
        await ctx.send(embed=embed)

@help.command()
async def moderation(ctx):
        em=discord.Embed(title="GruBot 3.0.0 Moderation Help Command", url="https://discord.com/oauth2/authorize?client_id=829110030736949298&scope=bot&permissions=8", description="The moderation help command for GruBot V.2")
        em.set_author(name="Akins", icon_url="https://cdn.discordapp.com/avatars/707643377621008447/8e56c7abb270316601cc1fc0f9c8c06a.png?size=1024")
        em.add_field(name="ban", value="Bans a specific user", inline=False)
        em.add_field(name="kick", value="Kicks a certain user", inline=False)
        em.add_field(name="unban", value="Unbans a certain user", inline=False)
        em.add_field(name="softban", value="Bans a certain user for a specified duration (in minutes)", inline=False)
        em.add_field(name="userinfo", value="Displays information about a user", inline=False)
        em.add_field(name="avatar", value="Displays a users avatar", inline=False)
        em.add_field(name="mute", value="Disallows a user speaking permissions for a specified mount of time (in minutes)", inline=False)
        em.add_field(name="purge", value="Deletes a specified number of messages", inline=False)
        em.add_field(name="serverstats", value="Displays the servers stats", inline=False)
        await ctx.send(embed=em)

@help.command()
async def fun(ctx):
        emb=discord.Embed(title="GruBot 3.0.0 Fun Help Command", url="https://discord.com/oauth2/authorize?client_id=829110030736949298&scope=bot&permissions=8", description="The music fun command for GruBot V.2")
        emb.set_author(name="Akins", icon_url="https://cdn.discordapp.com/avatars/707643377621008447/8e56c7abb270316601cc1fc0f9c8c06a.png?size=1024")
        emb.add_field(name="ping", value="Returns pong", inline=False)
        emb.add_field(name="source", value="Displays a link to the source code on repl.it", inline=False)
        emb.add_field(name="github", value="Displays a link to the source code on github, also available through Akins' connections page (If you're in a server with them) ", inline=False)
        emb.add_field(name="say", value="Makes the bot say a user inputted message, this is moderated dont get stupid.", inline=False)
        emb.add_field(name="serverstats", value="Displays statistics for the server")
        emb.add_field(name="holiday", value="Displays a holiday, and important piece of news for today")
        await ctx.send(embed=emb)

@help.command()
async def music(ctx):
        embe=discord.Embed(title="GruBot 3.0.1 Music Help Command", url="https://discord.com/oauth2/authorize?client_id=829110030736949298&scope=bot&permissions=8", description="The music help command for GruBot V.2")
        embe.set_author(name="Akins", icon_url="https://cdn.discordapp.com/avatars/707643377621008447/8e56c7abb270316601cc1fc0f9c8c06a.png?size=1024")
        embe.add_field(name="join", value="Makes the bot join your voice channel", inline=False)
        embe.add_field(name="summon", value="Summons the bot to your voice channel if it is in another channel", inline=False)
        embe.add_field(name="play", value="Plays a song in your current channel, or queues it to play", inline=False)
        embe.add_field(name="now", value="Displays the current song", inline=False)
        embe.add_field(name="queue", value="Displays the queue for songs", inline=False)
        embe.add_field(name="skip", value="Skips the current song", inline=False)
        embe.add_field(name="remove", value="Removes a song from the queue by number", inline=False)
        embe.add_field(name="pause", value="Pauses the current song", inline=False)
        embe.add_field(name="resume", value="Resumes a paused song", inline=False)
        embe.add_field(name="stop", value="Stops the current song and clears the queue", inline=False)
        embe.add_field(name="leave", value="Makes the bot leave the current channel", inline=False)
        embe.add_field(name="volume", value="Changes the bots volume", inline=False)
        embe.add_field(name="loop", value="Loops the current song", inline=False)
        await ctx.send(embed=embe)
    
bot.run(token)
