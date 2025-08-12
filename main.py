import os
import discord
from discord.ext import commands
import openai

# Load tokens from environment variables or placeholders
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN") or "PLACEHOLDER"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") or "PLACEHOLDER"

openai.api_key = OPENAI_API_KEY

intents = discord.Intents.default()
intents.message_content = True  # Required to read message content
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot connected as {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return  # Ignore bots including itself

    prompt = message.content

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # or "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": "You are a helpful Discord assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7,
        )
        reply = response.choices[0].message.content.strip()
    except Exception:
        reply = "Sorry, I couldn't process that."

    await message.channel.send(reply)

bot.run(DISCORD_TOKEN)
