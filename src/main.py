import os
import threading
from flask import Flask
import discord
from discord.ext import commands

# خادم ويب خفيف لإبقاء Render متصلاً بالبورت
app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

# إعدادات البوت
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

stock = {
    "حسابات": 10,
    "مفاتيح": 5,
    "بطاقات": 0
}

@bot.event
async def on_ready():
    print(f'تم تسجيل الدخول بنجاح باسم: {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong! البوت يعمل بنجاح 🟢')

@bot.command()
async def المخزون(ctx):
    embed = discord.Embed(title="📦 قائمة المخزون الحالية", color=0x00ff00)
    for item, qty in stock.items():
        status = f"{qty} متوفر" if qty > 0 else "❌ نافد"
        embed.add_field(name=item, value=status, inline=False)
    
    await ctx.send(embed=embed)

# تشغيل خادم الويب في الخلفية
threading.Thread(target=run_flask).start()

# تشغيل البوت
token = os.environ.get('DISCORD_TOKEN')
if token:
    bot.run(token)
