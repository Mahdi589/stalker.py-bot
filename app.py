import discord
from discord.ext import commands
from discord.utils import get


yo_bro_commands=['$help','$giverole','$hi','$game']

token='OTg1OTAwMzU4NDEwODI5ODc0.GUjG_A.dhOgqCd9JNKRiA7QwN9c7A80oKerJrBlnW-W74'
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

        if message.content not in yo_bro_commands:
            if message.author.id!=985900358410829874:
                print(f"{message.author} tried to use the {message.content} in the {message.channel} channel")
                await message.channel.send("```incorrect command\nUse the '$help' command```")

        

@bot.event
async def on_member_update(before, after):
    if str(before.status)!=str(after.status):
        print(f'{after.name} has changed hes status:{before.status.name}=>{after.status.name}')


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='KOS OMOK'))
bot.run(token)
