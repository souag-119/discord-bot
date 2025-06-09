import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot is ready: {bot.user}")

@bot.event
async def on_message(message):
    if message.channel.id == 1271242142374952970:  # غيّر لـ ID رومك
        if not (message.attachments and "title" in message.content.lower()):
            await message.delete()
            warning = await message.channel.send(f"🚫 <@{message.author.id}> لا يسمح بإرسال الرسائل العشوائية.\nالرجاء إرفاق صورة وكتابة `title`.")
            await warning.delete(delay=5)
    await bot.process_commands(message)

bot.run(os.getenv("DISCORD_TOKEN"))

