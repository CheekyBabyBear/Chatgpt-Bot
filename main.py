import os
import discord
from discord.ext import commands
import openai

# Load environment variables
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not DISCORD_TOKEN or not OPENAI_API_KEY:
    print("Error: Missing DISCORD_TOKEN or OPENAI_API_KEY environment variable.")
    exit(1)

# Initialize OpenAI client
openai.api_key = OPENAI_API_KEY

# Set up intents (adjust as needed)
intents = discord.Intents.default()
intents.message_content = True  # Needed to read message content

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")

@bot.command(name="ask")
async def ask_openai(ctx, *, question: str):
    """Ask OpenAI a question and get the answer."""
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=question,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
        answer = response.choices[0].text.strip()
        await ctx.reply(answer)
    except Exception as e:
        await ctx.reply(f"Error contacting OpenAI: {e}")

bot.run(DISCORD_TOKEN)
