import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members =  True

client = commands.Bot(command_prefix = 'your-prefix-here', intents=intents)

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.do_not_disturb)
  print("bot ok , online")

@client.command()
async def hello(ctx):
  await ctx.send("Hello!")

@client.event
async def on_member_join(member):
  channel = client.get_channel(welcome-channel-id-here)
  await channel.send("Hello And Welcome")

@client.event
async def on_member_remove(member):
  channel = client.get_channel(goodbye-channel-id-here)
  await channel.send("Goodbye :(")

@client.command()
async def status(ctx, *, status=None):
  await client.change_presence(activity=discord.Game(name=status))

@client.command()
async def members(ctx):
  await ctx.send(f'{ctx.guild.member_count} members!')

@client.command()
async def av(ctx, member:discord.Member):
    await ctx.send(member.avatar_url)
 
client.run('your-token-here')
