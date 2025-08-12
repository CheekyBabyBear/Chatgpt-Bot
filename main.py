import discord
from discord.ext import commands

# Define bot intents and prefix
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# --- Configuration ---
# DO NOT place your actual token or channel ID here.
# These will be set as secure environment variables on Railway.
BOT_TOKEN = 'PLACEHOLDER'
PROGRESS_CHANNEL_ID = 'not tricking me' 
# ---------------------

# Event listener for when the bot successfully connects to Discord
@bot.event
async def on_ready():
    """Confirms that the bot is logged in and ready."""
    print(f'Nexus Bot is ready. Logged in as {bot.user.name}')
    print('---')

# Simple command to check if the bot is responsive
@bot.command()
async def ping(ctx):
    """Responds with the bot's latency."""
    await ctx.send(f'Pong! My latency is {round(bot.latency * 1000)}ms')

# Command to send a project update to a specific channel
@bot.command()
async def update(ctx, *, message: str):
    """
    Sends a project update to the designated progress channel.
    Usage: !update <your progress message>
    """
    progress_channel = bot.get_channel(PROGRESS_CHANNEL_ID)
    if progress_channel:
        formatted_message = f"**{ctx.author.name} Update:**\n{message}"
        await progress_channel.send(formatted_message)
        await ctx.send("Update sent!", delete_after=5)
        await ctx.message.delete()
    else:
        await ctx.send("Error: Progress channel not found.")

# Command to assign a task to a collaborator
@bot.command()
async def task(ctx, collaborator: discord.Member, *, task_details: str):
    """
    Assigns a task to a collaborator.
    Usage: !task @user <task details>
    """
    await collaborator.send(f"**Task Assigned:**\nAssigned by: {ctx.author.name}\nTask: {task_details}")
    await ctx.send(f"Task assigned to {collaborator.mention}.")
    await ctx.message.delete()

# Run the bot with your token
bot.run(BOT_TOKEN)


