from email import message_from_string
import discord
from discord.ext import commands
from discord.utils import get
from datetime import datetime

yo_bro_commands=['$help','$giverole','$hi','$game','$add','$show']

stalked = []
authoriazed_authors=['Mahdi-Vagos-17.5-arbi#5815']
token=''
#bot=discord.Client()
prefix='$'

intents = discord.Intents.default()
intents.presences = True
intents.members = True
bot = commands.Bot(command_prefix='$',intents=intents)
@bot.event
async def on_message(message):
    if message.content[0]=='$':
        if message.content=='$hi':
            await message.channel.send('hello')

        if message.content=='$help':
            await message.channel.send('ASBA')

        if message.content=='$giverole':
            user=message.author
            role_id=986004073914449940
            role = get(message.guild.roles, name='Test')
            await user.add_roles(role,reason=None,atomic=True)
            await message.channel.send(user.id)

        if message.content=='$game':
            await message.channel.send(message.author.id)

        if message.content[1]=='add':
            if message.author in authoriazed_authors:
                stalked.append(message.content[1])
            else:
                await message.channel.send('ASPA')

        if message.content=='$show':
            print(message.author)
            if message.author in authoriazed_authors:
                await message.channel.send(stalked)
            else:
                await message.channel.send('ASPA')

        if message.content not in yo_bro_commands:
            msg=message.content[0]+message.content[1]+message.content[2]+message.content[3]
            if message.author.id!=985900358410829874 and msg!='$add':
                print(f"{message.author} tried to use the {message.content} in the {message.channel} channel")
                await message.channel.send("```incorrect command\nUse the '$help' command```")

        

@bot.event
async def on_member_update(before, after):
    if str(before.status)!=str(after.status):
        print(f"{after.name} has changed he's status:{before.status.name}=>{after.status.name}")
        if before.name in stalked:
            f=open('stalking_results.txt','a+')
            f.write(f"{before.name} has changed he's status:{before.status.name}=>{after.status.name} at {datetime.utcnow}")


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='KOS OMOK'))
bot.run(token)
