import discord
from discord.ext import commands, tasks
import os
from random import choice
import aiohttp
from random import randint
import wikipedia
import time
import datetime
import asyncio
import random
import typing

intents = discord.Intents.all()
prefixes = ["-"]
client = commands.Bot(command_prefix=prefixes, intents=intents)

status = ['Listening to -help', 'Make sure to read the rules!']

client.remove_command("help")

filter_words = ["fuck","bitch","pussy"]

#ready
@client.event
async def on_ready():
    change_status.start()
    print('Bot is ready.')
    
#status
@tasks.loop(seconds=20)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))

#auto role
@client.event
async def on_member_join(member):
  notrole=discord.utils.get(member.guild.roles, name='Not Verified')
  await member.add_roles(notrole)

#all roles command start

#cpp add command
@client.command()
async def add_cpp(ctx):
    cp = discord.utils.get(ctx.guild.roles, name='C++')
    cpbeg = discord.utils.get(ctx.guild.roles, name='C++ (Beginner)')
    await ctx.author.add_roles(cp)
    await ctx.author.add_roles(cpbeg)
    await ctx.channel.purge(limit=1) 
    await ctx.author.send(f'You have been given the required roles!')

#cpp remove command
@client.command()
async def remove_cpp(ctx):
    cp = discord.utils.get(ctx.guild.roles, name='C++')
    cpbeg = discord.utils.get(ctx.guild.roles, name='C++ (Beginner)')
    await ctx.author.remove_roles(cp)
    await ctx.author.remove_roles(cpbeg)
    await ctx.channel.purge(limit=1) 
    await ctx.author.send(f'You have been given the required roles!')

#c add command
@client.command()
async def add_c(ctx):
    ce = discord.utils.get(ctx.guild.roles, name='C')
    cebeg = discord.utils.get(ctx.guild.roles, name='C (Beginner)')
    await ctx.author.add_roles(ce)
    await ctx.author.add_roles(cebeg)
    await ctx.channel.purge(limit=1) 
    await ctx.author.send(f'You have been given the required roles!')

#c remove command
@client.command()
async def remove_c(ctx):
    ce = discord.utils.get(ctx.guild.roles, name='C')
    cebeg = discord.utils.get(ctx.guild.roles, name='C (Beginner)')
    await ctx.author.remove_roles(ce)
    await ctx.author.remove_roles(cebeg)
    await ctx.channel.purge(limit=1) 
    await ctx.author.send(f'You have been given the required roles!')

#py add command
@client.command()
async def add_py(ctx):
    p = discord.utils.get(ctx.guild.roles, name='Python')
    pbeg = discord.utils.get(ctx.guild.roles, name='Python (Beginner)')
    await ctx.author.add_roles(p)
    await ctx.author.add_roles(pbeg)
    await ctx.channel.purge(limit=1) 
    await ctx.author.send(f'You have been given the required roles!')

#py remove command
@client.command()
async def remove_py(ctx):
    p = discord.utils.get(ctx.guild.roles, name='Python')
    pbeg = discord.utils.get(ctx.guild.roles, name='Python (Beginner)')
    await ctx.author.remove_roles(p)
    await ctx.author.remove_roles(pbeg)
    await ctx.channel.purge(limit=1) 
    await ctx.author.send(f'You have been given the required roles!')

#ruby add command
@client.command()
async def add_ruy(ctx):
    r = discord.utils.get(ctx.guild.roles, name='Ruby')
    rbeg = discord.utils.get(ctx.guild.roles, name='Ruby (Beginner)')
    await ctx.author.add_roles(r)
    await ctx.author.add_roles(rbeg)
    await ctx.channel.purge(limit=1) 
    await ctx.author.send(f'You have been given the required roles!')

#ruby remove command
@client.command()
async def remove_ruby(ctx):
    r = discord.utils.get(ctx.guild.roles, name='Ruby')
    rbeg = discord.utils.get(ctx.guild.roles, name='Ruby (Beginner)')
    await ctx.author.remove_roles(r)
    await ctx.author.remove_roles(rbeg)
    await ctx.channel.purge(limit=1)
    await ctx.author.send(f'You have been given the required roles!')

#add PHP command
@client.command()
async def add_php(ctx):
    p = discord.utils.get(ctx.guild.roles, name='PHP')
    pbeg = discord.utils.get(ctx.guild.roles, name='PHP (Beginner)')
    await ctx.author.add_roles(p)
    await ctx.author.add_roles(pbeg)
    await ctx.channel.purge(limit=1) 
    await ctx.author.send(f'You have been given the required roles!')
    await ctx.autad_roles(p)
    await ctx.autaddd_roles(pbeg)

#remove PHP command
@client.command()
async def remove_php(ctx):
    p = discord.utils.get(ctx.guild.roles, name='PHP')
    pbeg = discord.utils.get(ctx.guild.roles, name='PHP(Beginner)')
    await ctx.author.remove_roles(p)
    await ctx.author.remove_roles(pbeg)
    await ctx.channel.purge(limit=1) 
    await ctx.author.send(f'You have been given the required roles!')

#add css command
@client.command()
async def add_css(ctx):
    p = discord.utils.get(ctx.guild.roles, name='CSS')
    pbeg = discord.utils.get(ctx.guild.roles, name='CSS(Beginner)')
    await ctx.author.add_roles(p)
    await ctx.author.add_roles(pbeg)
    await ctx.channel.purge(limit=1) 
    await ctx.author.send(f'You have been given the required roles!')

#remove css command
@client.command()
async def remove_css(ctx):
    p = discord.utils.get(ctx.guild.roles, name='CSS')
    pbeg = discord.utils.get(ctx.guild.roles, name='CSS (Beginner)')
    await ctx.author.remove_roles(p)
    await ctx.author.remove_roles(pbeg)
    await ctx.channel.purge(limit=1) 
    await ctx.author.send(f'You have been given the required roles!')

#Java add command
@client.command()
async def add_java(ctx):
    ce = discord.utils.get(ctx.guild.roles, name='Java')
    cebeg = discord.utils.get(ctx.guild.roles, name='Java (Beginner)')
    await ctx.author.add_roles(ce)
    await ctx.author.add_roles(cebeg)
    await ctx.channel.purge(limit=1) 
    await ctx.author.send(f'You have been given the required roles!')
    
#Java remove command
@client.command()
async def remove_java(ctx):
    ce = discord.utils.get(ctx.guild.roles, name='Java')
    cebeg = discord.utils.get(ctx.guild.roles, name='Java (Beginner)')
    await ctx.author.remove_roles(ce)
    await ctx.author.remove_roles(cebeg)
    await ctx.channel.purge(limit=1) 
    await ctx.author.send(f'You have been given the required roles!')

#Node.Js add command
@client.command()
async def add_node(ctx):
    ce = discord.utils.get(ctx.guild.roles, name='Node.Js')
    cebeg = discord.utils.get(ctx.guild.roles, name='Node.Js (Beginner)')
    await ctx.author.add_roles(ce)
    await ctx.author.add_roles(cebeg)
    await ctx.channel.purge(limit=1) 
    await ctx.author.send(f'You have been given the required roles!')

#Node.Js remove command
@client.command()
async def remove_node(ctx):
    ce = discord.utils.get(ctx.guild.roles, name='Node.Js')
    cebeg = discord.utils.get(ctx.guild.roles, name='Node.Js (Beginner)')
    await ctx.author.remove_roles(ce)
    await ctx.author.remove_roles(cebeg)
    await ctx.channel.purge(limit=1) 
    await ctx.author.send(f'You have been given the required roles!')

#Golang add command
@client.command()
async def add_golang(ctx):
    ce = discord.utils.get(ctx.guild.roles, name='Golang')
    cebeg = discord.utils.get(ctx.guild.roles, name='Golang (Beginner)')
    await ctx.author.add_roles(ce)
    await ctx.author.add_roles(cebeg)
    await ctx.channel.purge(limit=1) 
    await ctx.author.send(f'You have been given the required roles!')

#Golang remove command
@client.command()
async def remove_golang(ctx):
    ce = discord.utils.get(ctx.guild.roles, name='Golang')
    cebeg = discord.utils.get(ctx.guild.roles, name='Golang (Beginner)')
    await ctx.author.remove_roles(ce)
    await ctx.author.remove_roles(cebeg)
    await ctx.channel.purge(limit=1) 
    await ctx.author.send(f'You have been given the required roles!')

#SQL add command
@client.command()
async def add_sql(ctx):
    ce = discord.utils.get(ctx.guild.roles, name='SQL')
    cebeg = discord.utils.get(ctx.guild.roles, name='SQL (Beginner)')
    await ctx.author.add_roles(ce)
    await ctx.author.add_roles(cebeg)
    await ctx.channel.purge(limit=1) 
    await ctx.author.send(f'You have been given the required roles!')

#SQL remove command
@client.command()
async def remove_sql(ctx):
    ce = discord.utils.get(ctx.guild.roles, name='SQL')
    cebeg = discord.utils.get(ctx.guild.roles, name='SQL (Beginner)')
    await ctx.author.remove_roles(ce)
    await ctx.author.remove_roles(cebeg)
    await ctx.channel.purge(limit=1) 
    await ctx.author.send(f'You have been given the required roles!')

#HTML add command
@client.command()
async def add_html(ctx):
    ce = discord.utils.get(ctx.guild.roles, name='HTML')
    cebeg = discord.utils.get(ctx.guild.roles, name='HTML (Beginner)')
    await ctx.author.add_roles(ce)
    await ctx.author.add_roles(cebeg)
    await ctx.channel.purge(limit=1) 
    await ctx.author.send(f'You have been given the required roles!')

#HTML remove command
@client.command()
async def remove_html(ctx):
    ce = discord.utils.get(ctx.guild.roles, name='HTML')
    cebeg = discord.utils.get(ctx.guild.roles, name='HTML (Beginner)')
    await ctx.author.remove_roles(ce)
    await ctx.author.remove_roles(cebeg)
    await ctx.channel.purge(limit=1) 
    await ctx.author.send(f'You have been given the required roles!')

#roles command end

#goodbye event
@client.event
async def on_member_remove(member):

  em=discord.Embed(title="Goodbye",description=f"Seems like {member.name} left us. :sob:", color=discord.Color.red())
  
  em.set_image(url="https://i.gifer.com/5FD0.gif")

  channel = client.get_channel(783298898194202665)

  await channel.send(id="783298898194202665", embed=em)

#swear stopper
@client.event
async def on_message(msg):
  for word in filter_words:
    if word in msg.content:
      await msg.delete()
      await msg.channel.send(f"{msg.author.mention}, Swearing is not allowed in this server")

  await client.process_commands(msg)

#ping command
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


#clear command
@client.command(aliases=["cls", "purge"])
@commands.has_permissions(manage_messages=True, administrator=True)
async def clear(ctx, ammount: int):
    await ctx.channel.purge(limit=ammount + 1)
    await ctx.send(f'I have deleted {ammount} of messages', delete_after=5)
    return

#8ball command
@client.command(aliases=['8ball'])
async def _8ball(ctx, question):
    import random
    responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful.",]
    await ctx.send(f'{random.choice(responses)}')


#help command
@client.command(aliases=['h'])
async def help(ctx):
    helpEmbed = discord.Embed(tittle="Help Menu", color=ctx.author.color)
    helpEmbed.set_author(name="Help Menu:\nPrefix = '>'")
    helpEmbed.add_field(
        name="Moderation Command Menu",
        value="```Type -modHelp to open that```",
        inline=True)
    helpEmbed.add_field(
        name="Miscellaneous Command Menu",
        value="```Type -miscHelp to open that```",
        inline=True)
    helpEmbed.set_image(
      url="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/67401945-34fc-46b8-8e8f-1982847277d4/ddba22b-2fad9d00-1d3f-4ec8-a65d-199a09dfa4e1.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvNjc0MDE5NDUtMzRmYy00NmI4LThlOGYtMTk4Mjg0NzI3N2Q0XC9kZGJhMjJiLTJmYWQ5ZDAwLTFkM2YtNGVjOC1hNjVkLTE5OWEwOWRmYTRlMS5naWYifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ._-whxwEBEaTLWUvSWL80KTGiwpoy9dSPzXSRhfTAzeM"
    )

    await ctx.send(embed=helpEmbed)


#modHelp
@client.command()
async def modHelp(ctx):
    mod = discord.Embed(tittle="mod", color=ctx.author.color)
    
    mod.add_field(name="Moderation Command Menu", value="```-clear (ammount) : Deletes the specified ammount of messages from the channel```\n```-ban (user) (reasion) : Bans the specified user from the server```\n```-kick (user) (reason) : Kicks the specified user from the server```\n```-mute (user) (reason) : Mutes the specified user from the server```\n```-unmute (user) : Unmutes the specified user```\n```-announce (message) : Sends a announcemnt in sylish embed style```\n")
    
    mod.set_footer(text="More moderation commands will be added soon")
    
    await ctx.send(embed=mod)


#miscHelp
@client.command()
async def miscHelp(ctx):
    misc = discord.Embed(tittle="misc", color=ctx.author.color)
    
    misc.add_field(name="Miscellaneous Command Menu", value="```-ping : Tells the bot's latency```\n```-8ball (question) : Tells the answer of the asked question in a random yes/no answer```\n```-meme : Send a hot meme from reddit```\n```-userinfo (user) : Send information about mentioned user```\n```-define (querry) : Sends a definition of your querry from wikipedia```\n```-suggest (suggestion) : Sends a suggestion in the suggestion channel and it gets voted```\n")
    
    misc.set_footer(text="More miscellaneous commands will be added soon")
    
    await ctx.send(embed=misc)

#ban command
@client.command(aliases=['b'])
@commands.has_permissions(ban_members=True, administrator=True)
async def ban(ctx, member: discord.Member, *, reason="No reason provided"):
    await ctx.send(f'Banned {member} from the server.')
    await member.ban(reason=reason)


#kick command
@client.command(aliases=['k'])
@commands.has_permissions(kick_members=True, administrator=True)
async def kick(ctx, member: discord.Member, *, reason="No reason provided"):
    await ctx.send(f'Kicked {member} from the server.')
    await member.kick(reason=reason)

#unban command
@client.command(aliases=['ub'])
@commands.has_permissions(ban_members=True, administrator=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if(user.name, user.discriminator) == (member_name,member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
            return

    await ctx.send(member+" was not found")

#mute command
@client.command()
@commands.has_permissions(
    kick_members=True,
    manage_messages=True,
    administrator=True,
    manage_roles=True)
async def mute(ctx, member: discord.Member, mute_time: int, *, reason=None):
    if not member:
        await ctx.send("Who do you want me to mute?")
        return
    role = discord.utils.get(ctx.guild.roles, name="Muted")

    if not role:
        await ctx.guild.create_role(name='Muted')

    for channel in ctx.guild.channels:
        await channel.set_permissions(
            role,
            speak=False,
            send_messages=False,
            read_message_history=True,
            read_messages=True)

    await member.add_roles(role)
    await ctx.send(f"{member.mention} was muted for {reason}")
    await member.send(f"You were muted in **{ctx.guild}** for {reason}")

    await asyncio.sleep(mute_time)
    await member.remove_roles(role)
    await ctx.send(f"{member.mention} was unmuted")
    await member.send(f"You were unmuted in **{ctx.guild}**")

#unmute command
@client.command()
@commands.has_permissions(manage_roles=True, administrator=True)
async def unmute(ctx, member: discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.remove_roles(mutedRole)
    await ctx.send(f'Unmuted {ctx.members.mention}')
    await member.send(f'You have been unmuted from the server {ctx.guild.name}'
                      )


#meme command
@client.command()
async def meme(ctx):
    async with aiohttp.ClientSession() as cs:
        async with cs.get(
                'https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed = discord.Embed(title="Memes", color=discord.Color.orange())
            embed.set_image(url=res['data']['children'][random.randint(0, 25)]
                            ['data']['url'])
            await ctx.send(embed=embed)


#kill command
@client.command()
async def kill(ctx, user):
    k = random.randint(0, 5)
    if k == 0:
        await ctx.send(
            f'You challenged {user} to a fist fight to the death. You won.')
    if k == 2:
        await ctx.send(f'{user} had a mid air collision with nyan-cat')
    if k == 3:
        await ctx.send(
            f'{user} fell down a cliff while playing Pokemon Go. Good job on keeping your nose in that puny phone. :iphone:'
        )
    if k == 4:
        await ctx.send(
            f"{user} presses a random button and is teleported to the height of 100m, allowing them to fall to their inevitable death.\nMoral of the story: Don't go around pressing random buttons."
        )
    if k == 5:
        await ctx.send(
            f'{user} is sucked into Minecraft. {user}, being a noob at the so called Real-Life Minecraft faces the Game Over screen.'
        )

#announcemnt command
@client.command(aliases=["ann"])
@commands.has_permissions(administrator=True, manage_messages=True, manage_roles=True, ban_members=True, kick_members=True)
async def announce(ctx,*,message):
    anno = discord.Embed(tittle="ann", color=ctx.author.color)
    anno.add_field(name="Announcement", value=message)
    anno.set_footer(text=f"Announcement by {ctx.author.name}")
    await ctx.send(embed=anno)
    await ctx.send('@everyone', delete_after=3)

#define command
@client.command()
async def define(ctx,*, ask):
    definition = wikipedia.summary(ask, sentences=3, chars=1000, auto_suggest=False, redirect=True) 
    search = discord.Embed(color=ctx.author.color)
    search.add_field(name=ask, value=definition, inline=False)
    await ctx.send(embed=search)

#userinfo command
@client.command(aliases=["ui"])
async def userinfo(ctx, member: discord.Member):
  
  em=discord.Embed(color=member.color)

  em.set_author(name=f"{member.name}'s info")
  em.set_thumbnail(url=member.avatar_url)
  em.set_footer(text=f"Requested by {ctx.author.name}")

  em.add_field(name='Member Name', value=member.name)
  em.add_field(name="Member name in guild", value=member.display_name)

  em.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

  await ctx.send(embed=em)

#verify command
@client.command()
@commands.has_role("Not Verified")
async def verify(ctx):
  verifiedrole = discord.utils.get(ctx.guild.roles, name='Verified')
  await ctx.author.add_roles(verifiedrole)
  verify = discord.Embed(title="Verification",description="Congrats! You have been verified!", color=ctx.author.color)
  await ctx.send(embed=verify)
  await ctx.author.send(embed=verify)
  u = discord.utils.get(ctx.guild.roles, name='Not Verified')
  await ctx.author.remove_roles(u)
  wel = discord.Embed(title="Welcome", description=f"Welcome {ctx.author.name} to our server!")
  wel.set_image(url='https://i.pinimg.com/originals/b9/7d/c2/b97dc288d71e7938c1ce8b7faacdc9ac.gif')
  chl = client.get_channel(783298898194202665)
  await chl.send(embed=wel)

@client.command(aliases=['si'])
async def serverinfo(ctx):
  guild=ctx.guild

  em=discord.Embed(title=f"{guild.name} info", color=ctx.author.color)
  em.set_footer(text=f'Requested by {ctx.author.name}')
  em.add_field(name='Total members', value=f"{guild.member_count}")
  em.add_field(name="Owner", value=f"{guild.owner.name}")
  em.add_field(name="Server created on:", value=guild.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

  await ctx.send(embed=em)

#suggest command
@client.command()
async def suggest(ctx, *, message):
  em=discord.Embed(title="Suggestion", description=message,color=ctx.author.color)
  em.set_footer(text=f"Suggestion by {ctx.author.name}")
  channel = client.get_channel(785726236273672233)
  message_ = await channel.send(embed=em)
  await message_.add_reaction("✅")
  await message_.add_reaction("❎")

#youtube command
@client.command()
async def ytsearch(ctx,*,search):
  em = discord.Embed(title=f"Results of searching {search}....", description=f"https://www.youtube.com/results?search_query={search}")
  await ctx.send(embed=em)

#all the errors

#clear error
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
     em = discord.Embed(title = "Error", description = "Either you have used the command incorrecly or you dont have permission to use this command.", color = discord.Color.red())
     await ctx.send(embed=em, delete_after=5)
    

#8ball error
@_8ball.error
async def _8ball_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
     em = discord.Embed(title = "Error", description = "8ball didnt gave an answer cause you didnt even ask a question idiot", color = discord.Color.red())
     await ctx.send(embed=em, delete_after=5)
      
#ban error
@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
     em = discord.Embed(title = "Error", description = "Either you have used the command incorrecly or you dont have permission to use this command.", color = discord.Color.red())
     await ctx.send(embed=em, delete_after=5)

#kick error
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
     em = discord.Embed(title = "Error", description = "Either you have used the command incorrecly or you dont have permission to use this command.", color = discord.Color.red())
     await ctx.send(embed=em, delete_after=5)

#unban error
@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):

        em=discord.Embed(title="Error", description="Either you have used the command incorrecly or you dont have permission to use this command or that user is not banned at this server", color=discord.Color.red())

        await ctx.send(embed=em, delete_after=5)
        

#userinfo error
@userinfo.error
async def userinfo_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):

        em = discord.Embed(title = "Error", description = "Please pass all required arguments", color = discord.Color.red())

        await ctx.send(embed=em, delete_after=5)

#define error
@define.error 
async def define_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        em=discord.Embed(title="Error", description="Either you have used the command incorrecly or wikipedia cant find the definitation of that", color=discord.Color.red())
        await ctx.send(embed=em, delete_after=5)

#suggest error
@suggest.error 
async def poll_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        em=discord.Embed(title="Error", description="Please specify a poll message you want to use", color=discord.Color.red())
        await ctx.send(embed=em, delete_after=5)

#verify error
@verify.error 
async def verify_error(ctx, error):
    em=discord.Embed(title="Error", description="You are already verified!", color=discord.Color.red())
    await ctx.send(embed=em, delete_after=5)

#youtube error
@ytsearch.error
async def ytsearch_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    em=discord.Embed(title="Error", description="Please specify a thing to search")
    await ctx.send(embed=em, delete_after=5)

client.run(os.environ['DISCORD_TOKEN'])