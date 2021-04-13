#The following code imports the essential modules#
import discord
from discord.ext import commands
import time
from time import localtime, strftime
import requests
import json
import async_pokepy
import asyncio

client = await async_pokepy.connect()

#The following code defines the Fun class as a discord cog#
class Fun(commands.Cog):
    def __int__(self, bot):
        self.bot=bot
    
    #The following code returns pong to ping, commonly used as a test command#
    @commands.command(name='ping')
    async def _ping(ctx):
        await ctx.send("pong")
   
    #The following command links the repl.it source code for the bot#
    @commands.command(name='source')
    async def _source(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(title="Source Code", url='https://replit.com/@pewdrip/GruBot-300?v=1')
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
   
    #The following code adds a holiday command#
    @commands.command(name='holiday')
    async def _holiday(self, ctx):
      await ctx.message.delete()
      embed = discord.Embed(title="Holiday's for today!", description="13/4/21", color=discord.Colour.magenta())
      embed.add_field(name="National Grilled Cheese Sandwich Day:", value="Today is national Peach Cobbler day, If you like Ice Cream, Peaches, and Cobbler, today is the day for you.")
      embed.add_field(name="In other, much more important news.", value="Today President Biden has announced that he will decide whether or not to Withdraw U.S. troops from Afghanistan.")
      await ctx.send(embed=embed)
   
    #The following code displays basic server statistics#
    @commands.command(name='serverstats')
    async def _serverstats(self, ctx):
      user = ctx.message.author
      avatar = user.avatar_url
      embed=discord.Embed(description=f"Requested by - {ctx.message.author}", color=discord.Colour.magenta())
      embed.set_author(name=f"Server stats for - {ctx.guild.name}", icon_url=avatar)
      embed.add_field(name="Users:", value=ctx.guild.member_count, inline=False)
      embed.add_field(name="Channels:", value=len(ctx.guild.channels), inline=False)
      await ctx.send(embed=embed)
    
    #The following code allows users to get information about a pokemon#
    @commands.command(name='pokemon')
    async def _pokemon(self, ctx, pokemon):
			    try:
                    result = await client.get_pokemon(pokemon)
                except async_pokepy.NotFound:
                    fuzzy = await client.get_pagination("pokemon", limit=800).find_similar(name)

                    if not fuzzy:
                        await ctx.send("No Pokémon found by name {0}.".format(name))
                    else:
                        result = fuzzy[0]  #  The first result is always the most accurate.
                        await ctx.send("No Pokémon found by name {0}, did you mean {1}?".format(name, result))
                else:
                    await ctx.send("Found {0} which has {1} abilities and {2} moves!"
            .format(result, len(result.abilities), len(result.moves)))
			

   
        
#The following code ensure sthat the main.py file adds the code to our bot#
def setup(bot):
  bot.add_cog(Fun(bot))
