import discord
from discord.ext import commands
import os

# Define bot intents and prefix
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# --- Configuration ---
# Get the bot token and channel ID from environment variables
BOT_TOKEN = os.getenv('BOT_TOKEN')
PROGRESS_CHANNEL_ID = int(os.getenv('PROGRESS_CHANNEL_ID'))

# Check if the token and channel ID are set
if BOT_TOKEN is None:
    raise ValueError("BOT_TOKEN environment variable not set.")
if PROGRESS_CHANNEL_ID is None:
    raise ValueError("PROGRESS_CHANNEL_ID environment variable not set.")
# ---------------------

@bot.event
async def on_ready():
    print(f'Nexus Bot is ready. Logged in as {bot.user.name}')
    print('---')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! My latency is {round(bot.latency * 1000)}ms')

@bot.command()
async def update(ctx, *, message: str):
    progress_channel = bot.get_channel(PROGRESS_CHANNEL_ID)
    if progress_channel:
        formatted_message = f"**{ctx.author.name} Update:**\n{message}"
        await progress_channel.send(formatted_message)
        await ctx.send("Update sent!", delete_after=5)
        await ctx.message.delete()
    else:
        await ctx.send("Error: Progress channel not found.")

@bot.command()
async def task(ctx, collaborator: discord.Member, *, task_details: str):
    await collaborator.send(f"**Task Assigned:**\nAssigned by: {ctx.author.name}\nTask: {task_details}")
    await ctx.send(f"Task assigned to {collaborator.mention}.")
    await ctx.message.delete()

# Run the bot with the token from the environment variable
bot.run(BOT_TOKEN)
