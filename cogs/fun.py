#The following code imports the essential modules#
import discord
from discord.ext import commands
import time
from time import localtime, strftime

#The following code defines the Fun class as a discord cog#
class Fun(commands.Cog):
    def __int__(self, bot):
        self.bot=bot
    
    #The following code returns pong to ping, commonly used as a test command#
    @commands.command(name='ping')
    async def _ping(ctx):
        await ctx.send("pong")
    
    #The folowing code gives information on Wren#
    @commands.command(name='wren')
    async def _wren(self, ctx):
        await ctx.message.delete()
        await ctx.message.author.send("What a Faggot amiright?")
    
    #The following code does the sex, which I'll never do because I'm a programmer#
    @commands.command(name='sex')
    async def _sex(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(title="Gru touches your nono area UwU...")
        embed.set_image(url='https://cdn140.picsart.com/306455722075201.jpg?type=webp&to=min&r=640')
        await ctx.message.author.send(embed=embed)
    
    #The following code gives information on Akins#
    @commands.command(name='akins')
    async def _akins(self, ctx):
        await ctx.message.delete()
        await ctx.send("Akins is hot lol")
    
    #The following code gives information on DuckBot#
    @commands.command(name='duckbot')
    async def _duckbot(self, ctx):
        await ctx.message.delete()
        await ctx.send("DuckBot is gay, so is Akins")
    
    #The following command links the repl.it source code for the bot#
    @commands.command(name='source')
    async def _source(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(title="Source Code", url='https://replit.com/join/tacbunfb-pewdrip')
        await ctx.message.author.send(embed=embed)
    
    #The following command links the github repository for the bot#
    @commands.command(name='github')
    async def _github(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(title="GruBot Github Repo", url='https://github.com/Vigilantly-2328/grubot')
        await ctx.message.author.send(embed=embed)

    #The following command makes the bot say a user inputted message, with a failsafe to ensure that it isn't abused#
    @commands.command(name='say')
    async def _say(self, ctx, *, message):
        await ctx.message.delete()
        await ctx.send(message)
        print(f"{ctx.message.author} - {message} : " + strftime("%Y-%m-%d %H:%M:%S", localtime()))

#The following code ensure sthat the main.py file adds the code to our bot#
def setup(bot):
  bot.add_cog(Fun(bot))
