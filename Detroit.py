import discord
from discord.ext import commands, tasks
import os
from random import choice

intents = discord.Intents.all()
prefixes = [".","$","d!",";"]
client = commands.Bot(command_prefix=list(prefixes),intents = intents)

client = commands.Bot(command_prefix = prefixes)

status = ['Listening to .help', 'Listening to ;help', 'Listening to $help', 'Listening to d!help']

client.remove_command("help")

@client.event
async def on_ready():
	change_status.start()
	print('Bot is ready.')

@tasks.loop(seconds=20)
async def change_status():
	await client.change_presence(activity=discord.Game(choice(status)))

@client.command()
async def ping(ctx):
	await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases=["purge", "cls"])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, ammount):
	await ctx.channel.purge(limit=int(ammount))
	return

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

@client.command()
async def info(ctx):
	import random
	n = random.randint(0,2)
	if n == 0:
		myEmbed = discord.Embed(tittle="Information", color=0x00FFFF)
		myEmbed.add_field(name="Version Code:", value="```v1.0.0```", inline=False)
		myEmbed.add_field(name="Date Released:", value="```November 25th, 2020```", inline=False)
		myEmbed.add_field(name="Author:", value="```DarkLord#2292```", inline=False)
		myEmbed.set_author(name="Detroid")
		myEmbed.set_thumbnail(url="https://i.pinimg.com/originals/fd/a1/3b/fda13b9d6d88f25a9d968901d319216a.jpg")
	
		await ctx.send(embed=myEmbed)

	if n == 1:
		myEmbed = discord.Embed(tittle="Information", color=0xFFB6C1)
		myEmbed.add_field(name="Version Code:", value="```v1.0.0```", inline=False)
		myEmbed.add_field(name="Date Released:", value="```November 25th, 2020```", inline=False)
		myEmbed.add_field(name="Author:", value="```DarkLord#2292```", inline=False)
		myEmbed.set_author(name="Detroid")
		myEmbed.set_thumbnail(url="https://i.pinimg.com/originals/fd/a1/3b/fda13b9d6d88f25a9d968901d319216a.jpg")
	
		await ctx.send(embed=myEmbed)

	if n == 2:
		myEmbed = discord.Embed(tittle="Information", color=0x00FF00)
		myEmbed.add_field(name="Version Code:", value="```v1.0.0```", inline=False)
		myEmbed.add_field(name="Date Released:", value="```November 25th, 2020```", inline=False)
		myEmbed.add_field(name="Author:", value="```DarkLord#2292```", inline=False)
		myEmbed.set_author(name="Detroid")
		myEmbed.set_thumbnail(url="https://i.pinimg.com/originals/fd/a1/3b/fda13b9d6d88f25a9d968901d319216a.jpg")
	
		await ctx.send(embed=myEmbed)		

@client.command(aliases="h")
async def help(ctx):
	helpEmbed = discord.Embed(tittle="Help Menu", color=0x000000)
	helpEmbed.set_author(name="Help Menu:")
	helpEmbed.set_image(url="https://i.pinimg.com/originals/fd/a1/3b/fda13b9d6d88f25a9d968901d319216a.jpg")
	helpEmbed.add_field(name="Moderation Command Menu", value="```Type .mocd to open that```", inline=True)
	helpEmbed.add_field(name="Miscellaneous Command Menu", value="```Type .micd to open that```", inline=True)

	await ctx.send(embed=helpEmbed)

@client.command(aliases=['k'])
@commands.has_permissions(kick_members=True, administrator=True)
async def kick(ctx, member: discord.Member, *, reason="No reason provided"):
	await ctx.send(f'Kicked {member} from the server.')
	await member.kick(reason=reason)

@client.command(aliases=['b'])
@commands.has_permissions(ban_members=True, administrator=True)
async def ban(ctx, member: discord.Member, *, reason="No reason provided"):
	await ctx.send(f'Banned {member} from the server.')
	await member.ban(reason=reason)

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

@client.command()
async def mocd(ctx):
	modEmbed = discord.Embed(tittle="Moderation Command Menu", color=0xFFFF00)
	modEmbed.add_field(name="Moderation Command Menu", value="```.kick (user) (reason): Kicks a member from the server```\n```.ban (user) (reason): Bans a member from the server```\n```.unban (user): Unbans a banned user from the server```\n```.clear (ammount): Clears the specified amount of messages from that channel```\n")
	modEmbed.set_image(url="https://i.pinimg.com/originals/fd/a1/3b/fda13b9d6d88f25a9d968901d319216a.jpg")
	modEmbed.set_footer(text="More moderation commands will be added soon")
	await ctx.send(embed=modEmbed)

@client.command()
async def micd(ctx):
	misEmbed = discord.Embed(tittle="Miscellaneous Command Menu", color=0xFFFF00)
	misEmbed.add_field(name="Miscellaneous Command Menu", value="```.ping: Tells the bot ping```\n```.info: Tells information about the bot```\n```.8ball (question): Asks a question to the bot and the bot responds with random yes/no answer```\n```.kill (user_mention): Kills the mentioned user```\n```.invite: Gives the bot's invite link```")
	misEmbed.set_image(url="https://i.pinimg.com/originals/fd/a1/3b/fda13b9d6d88f25a9d968901d319216a.jpg")
	misEmbed.set_footer(text="More miscellaneous commands will be added soon")
	await ctx.send(embed=misEmbed)

@client.command(aliases=["i"])
async def invite(ctx):
	invEmbed = discord.Embed(tittle="Invite link of bot", color=0x00FFFF)
	invEmbed.add_field(name="Invite Link", value="[Click this to invite the bot](https://rb.gy/9wa5wa)")
	invEmbed.set_image(url="https://i.pinimg.com/originals/fd/a1/3b/fda13b9d6d88f25a9d968901d319216a.jpg")
	await ctx.send(embed=invEmbed)

@client.command()
async def kill(ctx, user):
	import random
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
		await ctx.send(f'{user} is sucked into Minecraft. Dank Memer, being a noob at the so called Real-Life Minecraft faces the Game Over screen.')

@client.command(aliases=["a"])
@commands.has_permissions(manage_roles=True)
async def addrole(ctx, role: discord.Role, user: discord.Member):
	await user.add_roles(role)
	addEmbed = discord.Embed(tittle="GiveRole", color=0xd0f0c0)
	addEmbed.set_author(name="Succesfully Done")
	await send(embed=addEmbed)

@client.command(aliases=["r"])
@commands.has_permissions(manage_roles=True)
async def removerole(ctx, role: discord.Role, user: discord.Member):
	await user.add_roles(role)
	removeEmbed = discord.Embed(tittle="RemoveRole", color=0xd0f0c0)
	removeEmbed.set_author(name="Succesfully Done")
	await send(embed=removeEmbed)

client.run(client.run(os.environ['DISCORD_TOKEN']))