#The following code imports any essential moudles#
import discord
from discord.ext import commands
import asyncio

#The following code creates the "Moderation" class, and defines it as a cog#
class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #The following code bans a user#
    @commands.command(name='ban')
    @commands.has_permissions(ban_members=True)
    async def _ban(self, ctx, user: discord.Member, *, reason=None):
        if reason == None:
            reason = "For being annoying"
        await user.ban(reason=reason)
        await user.send(f"You have been banned in {ctx.guild.name} for {reason}") 
        await ctx.send(f"{user} has been successfully banned by {ctx.message.author} for {reason}.", delete_after=5) 
    
    #The following code kicks a user#
    @commands.command(name='kick')
    @commands.has_permissions(kick_members=True)
    async def _kick(self, ctx, user: discord.Member, *, reason=None):
        if reason == None:
            reason = "For being annoying"
        await user.ban(reason=reason)
        await user.send(f"You have been banned in {ctx.guild.name} for {reason}")
        await ctx.send(f"{user} has been successfully kicked by {ctx.message.author} for {reason}.", delete_after=5)
    
    #The following code mutes a user for a certain duration of time (in minutes)#
    @commands.command(name='mute')
    @commands.has_permissions(manage_messages=True)
    async def _mute(self, ctx, user: discord.Member, duration: int, *, reason=None):
        if reason == None:
            reason = "For being annoying"
        time = duration*60
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")

        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted")  
            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
        else:
            await ctx.send("User is already muted.")
        embed = discord.Embed(title="muted", description=f"{member.mention} was muted ", colour=discord.Colour.light_gray())
        embed.add_field(name="reason:", value=reason, inline=False)
        await ctx.send(embed=embed)
        await member.add_roles(mutedRole, reason=reason)
        await member.send(f" you have been muted from: {guild.name} reason: {reason}")
        asyncio.sleep(time)
        await member.remove_roles(mutedRole)
        await member.send(f" you have unmuted from: - {guild.name}")
        embed = discord.Embed(title="Member Unmuted!", description=f" unmuted-{member.mention}",colour=discord.Colour.light_gray())
        await ctx.send(embed=embed, delete_after=5)
    
    #The following code bans a user for a certain amount of time (in minutes)#
    @commands.command(name='softban')
    @commands.has_permissions(ban_members=True)
    async def _softban(self, ctx, user: discord.Member, duration: int):
        time = duration*60
        await user.ban()
        await user.send(f"You have been banned in {ctx.guild} for {duration} seconds")
        await asyncio.sleep(time)
        await ctx.guild.unban(user)
        await user.send(f"You're now unbanned in {ctx.guild.name}!")
    
    #The following code unbans a user#
    @commands.command(name='unban')
    @commands.has_permissions(ban_members=True)
    async def _unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return

    #The following code gives the author information about a user#
    @commands.command(name='userinfo')
    async def _userinfo(self, ctx, *, member: discord.Member):
        roles = [role for role in member.roles if role != ctx.guild.default_role]
        embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)
        embed.set_author(name=f"User Info - {member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer (text=f"Requested by {ctx.author}")
        embed.add_field(name="ID", value=member.id)
        embed.add_field(name="Display Name", value=member.display_name)
        embed.add_field(name="Created at:", value=member.created_at.strftime("%a, %#d %B %Y, %I %M %p UTC"))
        embed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %#d %B %Y, %I %M %p UTC"))
        embed.add_field(name=f"(Roles, {len(roles)}", value=" ".join([role.mention for role in roles]))
        embed.add_field(name="Top Role:", value=member.top_role.mention)
        embed.add_field(name="Bot?", value=member.bot)
        await ctx.send(embed=embed)

    #The following code gives the author a users avatar#
    @commands.command(name='avatar')
    async def _avatar(self, ctx, *, member: discord.Member):
        embed=discord.Embed(title=f"{member.name}'s Avatar", color=member.color, timestamp=ctx.message.created_at)
        embed.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed=embed)

    #The following code deletes a certain number of messages#
    @commands.command(name='purge')
    @commands.has_permissions(manage_messages=True)
    async def _purge(ctx, amount):
        await ctx.delete_message()
        await ctx.channel.purge(amount=amount)
        await ctx.send(f"{ctx.message.author} has deleted {amount} messages", delete_after=3)  

#The following code ensures that our main.py file adds the cog to our bot#
def setup(bot):
  bot.add_cog(Moderation(bot))