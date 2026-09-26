import os
import discord
from discord.ext import commands

# إعداد الصلاحيات (Intents)
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# قائمة مؤقتة للمخزون (يمكنك تعديلها وإضافة المنتجات التي تريدها)
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
    """أمر للتأكد من أن البوت شغال"""
    await ctx.send('Pong! البوت يعمل بنجاح 🟢')

@bot.command()
async def المخزون(ctx):
    """عرض قائمة المخزون الحالية"""
    embed = discord.Embed(title="📦 قائمة المخزون الحالية", color=0x00ff00)
    for item, qty in stock.items():
        status = f"{qty} متوفر" if qty > 0 else "❌ نافد"
        embed.add_field(name=item, value=status, inline=False)
    
    await ctx.send(embed=embed)

# قراءة التوكن من متغيرات البيئة في Render
token = os.environ.get('DISCORD_TOKEN')

if token:
    bot.run(token)
else:
    print("خطأ: لم يتم العثور على DISCORD_TOKEN في متغيرات البيئة!")
