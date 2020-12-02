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
prefixes = ["$","d!","."]
client = commands.Bot(command_prefix=list(prefixes),intents = intents)

client = commands.Bot(command_prefix = prefixes)

status = ['Listening to .help', 'Listening to $help', 'Listening to d!help']

client.remove_command("help")

@client.event
async def on_ready():
	change_status.start()
	print('Bot is ready.')

@tasks.loop(seconds=20)
async def change_status():
	await client.change_presence(activity=discord.Game(choice(status)))

#meme command 
@client.command()
async def meme(ctx):
    async with ctx.channel.typing():
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://www.reddit.com/r/dankmemes/new.json?sort=hot,") as r:
                res = await r.json()
                embed = discord.Embed(title="Here is a meme", color=0x00FFFF)
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)
#ping command
@client.command()
async def ping(ctx):
	await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

#clear command
@client.command(aliases=["purge", "cls"])
@commands.has_permissions(manage_messages=True, administrator=True)
async def clear(ctx, amount:int):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'I have deleted {ammount} messages.', delete_after=5)
    return

#8ball command
@client.command(aliases=['8ball'])
async def _8ball(ctx, question):
	import random
	responses = ["It is certain.",
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
				"Very doubtful."]
	await ctx.send(f'{random.choice(responses)}')

#info command
@client.command(aliases=['i'])
async def info(ctx):
	import random
	n = random.randint(0,2)
	if n == 0:
		myEmbed = discord.Embed(tittle="Information", color=0x00FFFF)
		myEmbed.add_field(name="Detroit", value="Detroit is a multipurpose bot which gives you access to variety of features,like Fun commands and Moderation commands(Still in BETA mode)", inline=False)
		myEmbed.add_field(name="Version Code:", value="```v1.0.0```", inline=True)
		myEmbed.add_field(name="Date Released:", value="```November 25th, 2020```", inline=True)
		myEmbed.add_field(name="Bot Creator:", value="```DarkLord#2292```", inline=False)
		myEmbed.set_thumbnail(url="https://i.pinimg.com/originals/fd/a1/3b/fda13b9d6d88f25a9d968901d319216a.jpg")
		myEmbed.set_footer(text="Special thanks to RefinedDev#8759")	
		await ctx.send(embed=myEmbed)

	if n == 1:
		myEmbed = discord.Embed(tittle="Information", color=0x00FF00)
		myEmbed.add_field(name="Detroit", value="Detroit is a multipurpose bot which gives you access to variety of features,like Fun commands and Moderation commands(Still in BETA mode)", inline=False)
		myEmbed.add_field(name="Version Code:", value="```v1.0.0```", inline=True)
		myEmbed.add_field(name="Date Released:", value="```November 25th, 2020```", inline=True)
		myEmbed.add_field(name="Bot Creator:", value="```DarkLord#2292```", inline=False)
		myEmbed.set_thumbnail(url="https://i.pinimg.com/originals/fd/a1/3b/fda13b9d6d88f25a9d968901d319216a.jpg")
		myEmbed.set_footer(text="Special thanks to RefinedDev#8759")	
		await ctx.send(embed=myEmbed)

	if n == 2:
		myEmbed = discord.Embed(tittle="Information", color=0xFFB6C1)
		myEmbed.add_field(name="Detroit", value="Detroit is a multipurpose bot which gives you access to variety of features,like Fun commands and Moderation commands(Still in BETA mode)", inline=False)
		myEmbed.add_field(name="Version Code:", value="```v1.0.0```", inline=True)
		myEmbed.add_field(name="Date Released:", value="```November 25th, 2020```", inline=True)
		myEmbed.add_field(name="Bot Creator:", value="```DarkLord#2292```", inline=False)
		myEmbed.set_thumbnail(url="https://i.pinimg.com/originals/fd/a1/3b/fda13b9d6d88f25a9d968901d319216a.jpg")
		myEmbed.set_footer(text="Special thanks to RefinedDev#8759")	
		await ctx.send(embed=myEmbed)	

#help command
@client.command(aliases=['h'])
async def help(ctx):
	helpEmbed = discord.Embed(tittle="Help Menu", color=ctx.author.color)
	helpEmbed.set_author(name="Help Menu:\nPrefixes = '.'  'd!'  '$'")
	helpEmbed.add_field(name="Support Us!", value="```Type .supportme```", inline=False)
	helpEmbed.add_field(name="Info about us", value="```Type .info```", inline=False)
	helpEmbed.add_field(name="Moderation Command Menu", value="```Type .mocd to open that```", inline=True)
	helpEmbed.add_field(name="Miscellaneous Command Menu", value="```Type .micd to open that```", inline=True)

	await ctx.send(embed=helpEmbed)

#kick command
@client.command(aliases=['k'])
@commands.has_permissions(kick_members=True, administrator=True)
async def kick(ctx, member: discord.Member, *, reason="No reason provided"):
	await ctx.send(f'Kicked {member} from the server.')
	await member.kick(reason=reason)

#ban command
@client.command(aliases=['b'])
@commands.has_permissions(ban_members=True, administrator=True)
async def ban(ctx, member: discord.Member, *, reason="No reason provided"):
	await ctx.send(f'Banned {member} from the server.')
	await member.ban(reason=reason)

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

#Moderation Menu Command
@client.command(aliases=['mo'])
async def mocd(ctx):
	modEmbed = discord.Embed(tittle="Moderation Command Menu", color=0xFFFF00)
	modEmbed.add_field(name="Moderation Command Menu", value="```.kick (user) (reason): Kicks a member from the server```\n```.ban (user) (reason): Bans a member from the server```\n```.unban (user): Unbans a banned user from the server```\n```.clear (ammount): Clears the specified amount of messages from that channel```\n```.addrole (role) (user): Adds the specified role to the specified user```\n```.removerole (role) (user): Removes the specified role from the specified user```\n```.mute (user): Mutes the specified user```\n```.unmute (user): Unmutes the specified user```\n```.giveaway: Starts a giveaway!```\n")
	modEmbed.set_footer(text="More moderator commands will be added soon")
	await ctx.send(embed=modEmbed)

#Miscellaneous Command Menu
@client.command(aliases=['mi'])
async def micd(ctx):
	misEmbed = discord.Embed(tittle="Miscellaneous Command Menu", color=0xFFFF00)
	misEmbed.add_field(name="Miscellaneous Command Menu", value="```.ping: Tells the bot latency```\n```.8ball (question): Asks a question to the bot and the bot responds with random yes/no answer```\n```.kill (user_mention): Kills the mentioned user```\n```.avatar (user): Gives the specified user's profile picture or avatar```\n```.meme: Sends a hot meme from reddit```\n```.define (query): Shows the definition of query you ask```\n")
	misEmbed.set_footer(text="More miscellaneous commands will be added soon")
	await ctx.send(embed=misEmbed)

#support command
@client.command(aliases=["sup"])
async def supportme(ctx):
	invEmbed = discord.Embed(tittle="Invite link of bot", color=0x00FFFF)
	invEmbed.add_field(name="Invite Link", value="[Click this to invite the bot](https://discord.com/oauth2/authorize?client_id=781379286924918785&scope=bot&permissions=1372925175)", inline=False)
	invEmbed.add_field(name="Server Link", value="[Click this to join the server](https://discord.gg/KJ6Twwkafw)", inline=False)
	invEmbed.add_field(name="Upvote Link", value="[Click this to upvote us!](https://top.gg/bot/781379286924918785)", inline=False)
	await ctx.send(embed=invEmbed)

#kill command
@client.command()
async def kill(ctx, user):
	k = random.randint(0,5)
	if k == 0:
		await ctx.send(f'You challenged {user} to a fist fight to the death. You won.')
	if k == 2:
		await ctx.send(f'{user} had a mid air collision with nyan-cat')
	if k == 3:
		await ctx.send(f'{user} fell down a cliff while playing Pokemon Go. Good job on keeping your nose in that puny phone. :iphone:')
	if k == 4:
		await ctx.send(f"{user} presses a random button and is teleported to the height of 100m, allowing them to fall to their inevitable death.\nMoral of the story: Don't go around pressing random buttons.")
	if k == 5:
		await ctx.send(f'{user} is sucked into Minecraft. {user}, being a noob at the so called Real-Life Minecraft faces the Game Over screen.')

#addrole command
@client.command(aliases=["a"])
@commands.has_permissions(manage_roles=True, administrator=True)
async def addrole(ctx, role: discord.Role, user: discord.Member):
	await user.add_roles(role)
	await ctx.send(f'Succesfully Done')

#removerole command
@client.command(aliases=["r"])
@commands.has_permissions(manage_roles=True, administrator=True)
async def removerole(ctx, role: discord.Role, user: discord.Member):
	await user.remove_roles(role)
	await ctx.send(f'Succesfully Done')

#avatar command    
@client.command()
async def avatar(ctx, *, member: discord.Member=None):
    if not member:
        member = ctx.message.author
    userAvatar = member.avatar_url
    await ctx.send(userAvatar)

#mute command
@client.command(aliases=["m"])
@commands.has_permissions(manage_roles=True, administrator=True)
async def mute(self, ctx, members: commands.Greedy[discord.Member],
               mute_minutes: typing.Optional[int] = 0, *, reason = "No reason provided"):
    if not members:
        await ctx.send(f"You need to name someone to mute")
        return

    guild = ctx.guild
    muted_role = discord.utils.get(guild.roles, name="Muted")

    if not muted_role:
    	muted_role = await guild.create_role(name="Muted")

    	for channel in guild.channels:
    		await channel.set_permissions(muted_role, speak=False, send_messages=False, read_history=True, read_messages=True)

    for member in members:
        if self.bot.user == member:
            embed = discord.Embed(title = "You can't mute me, I'm an almighty bot")
            await ctx.send(embed = embed)
            continue
       	if mute_minutes == 0:
        	await member.add_roles(muted_role, reason = reason)
        	await ctx.send(f'{member.mention} has been muted by {ctx.author} for {reason} permanently')
        if mute_minutes > 0:
        	await member.add_roles(muted_role, reason = reason)
        	await ctx.send(f'{member.mention} has been muted by {ctx.author} for {reason} for {mute_minutes}.')
    if mute_minutes > 0:
        await asyncio.sleep(mute_minutes * 60)
        for member in members:
            await member.remove_roles(muted_role, reason = "time's up ")
#unmute command
@client.command()
@commands.has_permissions(manage_roles=True, administrator=True)
async def unmute(ctx, member: discord.Member):
	mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

	await member.remove_roles(mutedRole)
	await ctx.send(f'Unmuted {member.mention}')
	await member.send(f'You have been unmuted from the server {guild.name}')

def convert(time):
	pos = ["s","m","h","d"]

	time_dict = {"s" : 1, "m" : 60, "h" : 3600, "d" : 3600*24}

	unit = time[-1]

	if unit not in pos:
		return -1
	try:
		val = int(time[:-1])
	except:
		return -2

	return val * time_dict[unit]

#giveaway command
@client.command()
@commands.has_permissions(manage_roles=True, administrator=True, manage_channels=True)
async def giveaway(ctx):
	await ctx.send("Lets start with giveaway! Answer these questions within 20 seconds")

	questions = ["Which channel should it be hosted in?",
				"What should be the duration of the giveaway? (s|m|h|d)",
				"What is the prize of the giveaway?"]

	answers = []

	def check(m):
		return m.author == ctx.author and m.channel == ctx.channel

	for i in questions:
		await ctx.send(i)

		try:
			msg = await client.wait_for('message', timeout=20.0, check=check)
		except asyncio.TimeoutError:
			await ctx.send('You didnt\'t answer in time, please be quicker next time!')
			return
		else:
			answers.append(msg.content)

	try:
		c_id = int(answers[0][2:-1])
	except:
		await ctx.send(f"You didn't mention a channel properly. Do it like this {ctx.channel.mention} next time.")
		return

	channel = client.get_channel(c_id)

	time = convert(answers[1])
	if time == -1:
		await ctx.send(f"You didn't answer the time with proper unit. Use (s|m|h|d)")
		return
	elif time == -2:
		await ctx.send(f"The time must be an integer. Please enter an integer next time.")
		return

	prize = answers[2]

	await ctx.send(f"The Giveaway will be in {channel.mention} and it will last {answers[1]} seconds!")


	embed = discord.Embed(tittle = "Giveaway!", description = f"{prize}", color = ctx.author.color)
	embed.add_field(name = "Hosted by:", value= ctx.author.mention)
	embed.set_footer(text = f"Ends {answers[1]} from now!")

	my_msg = await channel.send(embed=embed)

	await my_msg.add_reaction("🎉")

	await asyncio.sleep(time)

	new_msg = await channel.fetch_message(my_msg.id)

	users = await new_msg.reactions[0].users().flatten()
	users.pop(users.index(client.user))

	winner = random.choice(users)

	await channel.send(f"Congratulation! {winner.mention} won {prize}!")

#reroll command
@client.command()
@commands.has_permissions(manage_roles=True, administrator=True, manage_channels=True)
async def reroll(ctx, channel : discord.TextChannel, id_ : int):
	try:
		new_msg = await channel.fetch_message(id_)
	except:
		await ctx.send("The id was entered incorrectly")
		return

	users = await new_msg.reactions[0].users().flatten()
	users.pop(users.index(client.user))

	winner = random.choice(users)

	await channel.send(f"Congratulation! {winner.mention} won {prize}!")

#define command
@client.command()
async def define(ctx,*, ask):
	definition = wikipedia.summary(ask, sentences=3, chars=1000, auto_suggest=False, redirect=True)	
	search = discord.Embed(color=ctx.author.color)
	search.add_field(name=ask, value=definition, inline=False)
	await ctx.send(embed=search)

#all the errors		

#clear error
@clear.error
async def clear_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send('Please specify an ammount of messages to delete.', delete_after=5)

#8ball error
@_8ball.error
async def _8ball_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send('8ball didnt gave an answer because you didnt even asked a question idiot.', delete_after=5)

#ban error
@ban.error
async def ban_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send('Either you have used the command wrongly or you dont have permission to use this command.', delete_after=5)

#kick error
@kick.error
async def kick_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send('Either you have used the command wrongly or you dont have permission to use this command.', delete_after=5)

#unban error
@unban.error
async def unban_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send('Either you have used the command wrongly or you dont have permission to use this command or that user is not banned at this server', delete_after=5)

#define error
@define.error 
async def define_error(ctx, error):
	if isinstance(error. commands.MissingRequiredArgument):
		await ctx.send('Either you have used the command wrongly or bot cant find definition of that on wikipedia')
		
client.run(os.environ['DISCORD_TOKEN'])