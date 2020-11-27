import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '.')

client.remove_command("help")

@client.event
async def on_ready():
	print('Bot is ready.')
	await client.change_presence(status=discord.Status.online, activity=discord.Game('Listening to .help'))

@client.command()
async def ping(ctx):
	await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def clear(ctx, ammount):
	await ctx.channel.purge(limit=int(ammount))

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
		myEmbed = discord.Embed(tittle="Current Version                                           ", color=0x00FFFF)
		myEmbed.add_field(name="Version Code:", value="v1.0.0                                     ", inline=False)
		myEmbed.add_field(name="Date Released:", value="November 25th, 2020                       ", inline=False)
		myEmbed.add_field(name="Author:", value="DarkLord#2292                                    ", inline=False)
		myEmbed.set_author(name="Detroid                                                          ")
	
		await ctx.send(embed=myEmbed)

	if n == 1:
		myEmbed = discord.Embed(tittle="Current Version                                           ", color=0xFFB6C1)
		myEmbed.add_field(name="Version Code:", value="v1.0.0                                     ", inline=False)
		myEmbed.add_field(name="Date Released:", value="November 25th, 2020                       ", inline=False)
		myEmbed.add_field(name="Author:", value="DarkLord#2292                                    ", inline=False)
		myEmbed.set_author(name="Detroid                                                          ")
	
		await ctx.send(embed=myEmbed)

	if n == 2:
		myEmbed = discord.Embed(tittle="Current Version                                           ", color=0x00FF00)
		myEmbed.add_field(name="Version Code:", value="v1.0.0                                     ", inline=False)
		myEmbed.add_field(name="Date Released:", value="November 25th, 2020                       ", inline=False)
		myEmbed.add_field(name="Author:", value="DarkLord#2292                                    ", inline=False)
		myEmbed.set_author(name="Detroid                                                          ")
	
		await ctx.send(embed=myEmbed)		

@client.command()
async def help(ctx):
	helpEmbed = discord.Embed(tittle="Help Menu                                                   ", color=0x000000)
	helpEmbed.set_author(name="Help Menu                                                          ")
	helpEmbed.set_thumbnail(url="https://i.pinimg.com/originals/fd/a1/3b/fda13b9d6d88f25a9d968901d319216a.jpg")
	helpEmbed.add_field(name="Moderation Command                                                  ", value=";clear", inline=False)
	helpEmbed.add_field(name="Miscellaneous commands", value=";ping, ;8ball, ;info                ")

	await ctx.send(embed=helpEmbed)

@client.command()
@commands.has_permissions(kick_members=True, administrator=True)
async def kick(ctx, member: discord.Member, *, reason=None):
	await member.kick(reason=reason)
	await ctx.send(f'Kicked {member} from the server.')

@client.command()
@commands.has_permissions(ban_members=True, administrator=True)
async def ban(ctx, mem: discord.Member, *, reason=None):
	await user.ban(reason=reason)
	await ctx.send(f'Banned {mem} from the server.')

@client.command(aliases=['ub'])
@commands.has_permissions(ban_members=True, administrator=True)
async def unban(ctx, *, member):
	banned_users = await ctx.guild.bans()
	member_name, member_disc = member.split('#')

	for banned_entry in banned_users:
		user = banned_entry.user

		if(user.name, user.discrminator) == (member_name,member_disc):

			await ctx.guild.unban(user)
			await ctx.send(member_name + " has been unbanned")
			return

	await ctx.send(member+" was not found")
	
client.run(os.environ['DISCORD_TOKEN'])