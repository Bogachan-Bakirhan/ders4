import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def sa(ctx):
    await ctx.send(f'As, hoşgeldin')

@bot.command()
async def bye(ctx):
    await ctx.send(f'Görüşürüz :)')

@bot.command()
async def bb(ctx):
    await ctx.send(f'bb')

@bot.command()
async def merhaba(ctx):
    await ctx.send(f'Merhaba!')


@bot.command()
async def komik(ctx):
    await ctx.send(f'AZQWSXEDCRFVTGBYHUNJIMKOÖLÇPŞĞİAZWSXEDCRTVBYNUIMJKOÖLPÇŞĞ')

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'Sunucuya hoş geldin {member.mention} !'
            await guild.system_channel.send(to_send)


intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)
client.run('Token')



bot.run("Token")
