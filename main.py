import os
import discord
from discord.ext import commands
import openai

# Load tokens from environment variables for safety
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN") or "MTQwNDgyMzI2OTk4NjUzMzUwNw.GQWTUI.fi8BO5xGidVYaC83YBiUYA85DHIHybXpHlliWw"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") or "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"

openai.api_key = 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

intents = discord.Intents.default()
intents.message_content = True  # Required to read message content
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot connected as {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return  # Ignore other bots and self

    # You can restrict it to certain channels or mentions if you want

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
    except Exception as e:
        reply = "Sorry, I couldn't process that."

    await message.channel.send(reply)

bot.run(DISCORD_TOKEN)
