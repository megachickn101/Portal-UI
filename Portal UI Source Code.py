import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '#')
client.remove_command('help')

def is_it_me(ctx):
	return ctx.author.id == <MYID>

@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.online, activity=discord.Game('use #help or #FAQ'))
	print('Portals Opened')

@client.command()
async def help(ctx):
	embed = discord.Embed(title='Portal UI Help', description='A New Way To Find Your Favorite Servers', colour=discord.Color.blue(), url= 'https://www.google.com')

	embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
	embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
	embed.set_image(url='https://cdn.discordapp.com/attachments/684422288178937882/690680255341658213/sketch-1584741380936.png')
	embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/684422288178937882/690680255341658213/sketch-1584741380936.png')
	
	embed.add_field(name='#listDiscordSummons', value='List Of Discord Servers You Can Pull And Their Commands')
	embed.add_field(name='#listWebSummons', value='List Of Websites You Can Pull And Their Commands')
	embed.add_field(name='#listDiscordPortalList', value='Lists ALL Discord Invites In Our Database!)')
	embed.add_field(name='#listWebPortalList', value='List ALL Websites In Our Database')
	embed.add_field(name='#connect<Website Or Server>',value='Gives you an invite to the server or the link to the website')
	embed.add_field(name='#sudoDiscordIPs', value='IPs Of The Discord Portals')
	embed.add_field(name='#sudoWebIPs', value='IPs Of The Web Portals')

	await ctx.send(embed=embed)

@client.command()
async def FAQ(ctx):
	embed = discord.Embed(title='Portal UI FAQ', description='Our FAQ', colour=discord.Color.blue(), url= 'https://www.google.com')

	embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
	embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
	embed.set_image(url='https://cdn.discordapp.com/attachments/684422288178937882/690680255341658213/sketch-1584741380936.png')
	embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/684422288178937882/690680255341658213/sketch-1584741380936.png')

	embed.add_field(name='Q: Are There Any Easter Eggs?', value='A: No, Just A Few Hidden Portals ;)', inline=False)
	embed.add_field(name='Q: HOW DO I USE PORTAL UI', value='A: Try #help', inline=False)
	embed.add_field(name='Q: My SeRvEr IsNt On YoUr BoT :(', value='A: Ok, chill... Use #register<Name Of Server and Unlimited Invite Link>', inline=False)
	embed.add_field(name='Q: My FaVoRiTe WeBsIte IsNt On YoUr BoT!!!!',value='Ok, Do The Same As Adding Server. Use #register<WebsiteUrl>', inline=False)
	embed.add_field(name='Q: Your Commands Arent Working!!',value='A: They Do, Youre just doing it wrong', inline=False)
	embed.add_field(name='Q: Ok! I TRIPLE CHECKED THe COMMAND I INPUTTED!! BUT IT STILL ISNT WORKING',value='DM me then, Ill check the output and see what happened', inline=False)
	embed.add_field(name='Q: Your Bot Sucks',value='A: Can you do better?', inline=False)

	await ctx.send(embed=embed)

@client.command()
async def listDiscordSummons(ctx):
	embed = discord.Embed(title='Discord Portal Summons', description='Discord Summoning Commands', colour=discord.Color.blue(), url= 'https://www.google.com')

	embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
	embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
	embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/684422288178937882/690680255341658213/sketch-1584741380936.png')

	embed.add_field(name='<SERVER>', value='connect<SERVER>', inline=False)

	await ctx.send(f'Discord Summons Sent!')
	await ctx.author.send(embed=embed)

@client.command()
async def listWebSummons(ctx):
	embed = discord.Embed(title='Web Portal Summons', description='Web Summoning Commands', colour=discord.Color.blue(), url= 'https://www.google.com')

	embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
	embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
	embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/684422288178937882/690680255341658213/sketch-1584741380936.png')

	embed.add_field(name='<WEBSITE>', value='connect<WEBSITE>', inline=False)

	await ctx.send(f'Web Summons Sent!')
	await ctx.author.send(embed=embed)

@client.command()
async def listDiscordPortalList(ctx):
	embed = discord.Embed(title='Portal UI List', description='List Of All Servers In The Portal UI Database', colour=discord.Color.blue(), url= 'https://www.google.com')

	embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
	embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
	embed.set_image(url='https://cdn.discordapp.com/attachments/684422288178937882/690680255341658213/sketch-1584741380936.png')
	embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/684422288178937882/690680255341658213/sketch-1584741380936.png')

	embed.add_field(name='<SERVER>', value='<INVITE>', inline=False)

	await ctx.send(f'Portal List Sent!')
	await ctx.author.send(embed=embed)

@client.command()
async def listWebPortalList(ctx):
	embed = discord.Embed(title='Web Portals', description='List Of All Websites In The Portal UI Database', colour=discord.Color.blue(), url= 'https://www.google.com')

	embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
	embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
	embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/684422288178937882/690680255341658213/sketch-1584741380936.png')

	embed.add_field(name='<WEBSITE>', value='<LINK>', inline=False)

	await ctx.send(f'Portal List Sent!')
	await ctx.author.send(embed=embed)

@client.command()
async def sudoDiscordIPs(ctx):
	embed = discord.Embed(title='Portal UI Discord IPs', description='A New Way To Find Your Favorite Servers', colour=discord.Color.blue(), url= 'https://www.google.com')

	embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
	embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
	embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/684422288178937882/690680255341658213/sketch-1584741380936.png')

	embed.add_field(name='<SERVER>', value='<IP>', inline=False)

	await ctx.send('IPs Sent!')
	await ctx.author.send(embed=embed)

@client.command()
async def sudoWebIPs(ctx):
	embed = discord.Embed(title='Portal UI Web IPs', description='A New Way To Find Your Favorite Websites', colour=discord.Color.blue(), url= 'https://www.google.com')

	embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
	embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
	embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/684422288178937882/690680255341658213/sketch-1584741380936.png')

	embed.add_field(name='<WEBSITE>', value='<IP>', inline=False)

	await ctx.send(f'IPs Sent!')
	await ctx.author.send(embed=embed)

@client.command()
async def register(ctx, *, message, amount=1):
	await ctx.channel.purge(limit=amount)
	await ctx.send(f'Server Info Sent!!!')
	print(f'Feedback: {message}')
	return

@client.command(aliases=['<IP>'])
async def connect<Server>(ctx):
	await ctx.send(f'<INVITE>')
	return

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@client.command(aliases=['<IP>'])
async def connect<WEBSITE>(ctx):
	await ctx.send(f'<WEBSITE>')
	return

#*
@client.command()
@commands.check(is_it_me)
async def sudoClosePortal(ctx):
	await client.close()


client.run("TOKEN")