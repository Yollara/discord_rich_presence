import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

    # Mudar o status para "Jogando ..."
    await bot.change_presence(activity=discord.Game(name="Minecraft"))

    # Ou outro tipo de status:
    # await bot.change_presence(activity=discord.Streaming(name="Minha Live", url="https://twitch.tv/seu_canal"))
    # await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Spotify"))
    # await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="um filme"))

bot.run("SEU_TOKEN_AQUI")