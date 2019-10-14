import discord
from discord.ext import commands
from discord.ext.commands import Bot

TOKEN = "NTE3MzEwNjQyNjg5MTQ2ODkz.XaSYiw.COpQSKmBWLis5SKOTO95TYso-vA"
BOT_PREFIX = ("&")
bot = commands.Bot(command_prefix=BOT_PREFIX, description='Hi')

@bot.command(pass_context=True)
async def userping(ctx, message):
    for members in bot.get_all_members():
        try:

                embed = discord.Embed(title="Epic title", description=message, color=ctx.message.author.top_role.colour)
                embed.set_footer(text="your daddy▪️ {}".format(ctx.message.created_at)[:-10], icon_url=(ctx.message.author.avatar_url))

                y=0
                x = y
                y = x + 1
                await members.send(embed=embed)
                await ctx.send("Sended {} messages!".format(y))
        except:
            continue


bot.run('Token')
