import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"تم تسجيل الدخول بنجاح باسم: {bot.user}")

@bot.command()
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        if ctx.voice_client is not None:
            await ctx.voice_client.move_to(channel)
        else:
            await channel.connect()
        await ctx.send(f"دخلت الروم: **{channel.name}** وبجلس فيه 24 ساعة!")
    else:
        await ctx.send("لازم تدخل روم صوتي أول عشان ألحقك!")

@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("طلعت من الروم الصوتي.")
    else:
        await ctx.send("أنا أصلاً مو في روم صوتي.")

bot.run(os.environ['TOKEN'])