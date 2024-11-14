import discord
import mysql.connector
from discord.ext import commands
from config import bot_token

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='>', intents=intents)

dbconfig = {'host': '127.0.0.1',
            'user': 'root',
            'password': 'Vlood2008',
            'database': 'race_game'}

@bot.command()
async def reg(ctx, name = None):
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    _SQL = '''select * from users where name = (%s)'''
    cursor.execute(_SQL, (name,))
    users_name = cursor.fetchall()
    cursor.close()
    conn.close()
    if users_name == []:
        await ctx.send('this user doesnt exist')
    else:
        await ctx.send('Id: ' + str(users_name[0][0]) + ', Name: ' + users_name[0][1] + ' Registered!')

@bot.command()
async def newuser(ctx, name = None):
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    _SQL = '''select * from users where name = (%s)'''
    cursor.execute(_SQL, (name,))
    users_name = cursor.fetchall()

    if users_name == []:
        _SQL = '''insert into users (name) values (%s)'''
        cursor.execute(_SQL, (name,))
        conn.commit()
        await ctx.send('user '+ name + ' the user has been registered!')
    else:
        await ctx.send('the user is already registered!')
    cursor.close()
    conn.close()




bot.run(bot_token)

