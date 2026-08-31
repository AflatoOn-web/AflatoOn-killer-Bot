import os
import random

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

# Quotes
QUOTES = [
    "Believe in yourself. You are capable of amazing things. ❤️🔥",
    "Small steps every day lead to big results. 🚀",
    "Don't stop when you're tired. Stop when you're done. 💪",
    "Your future is created by what you do today. ✨",
    "Success starts with believing that you can. 🏆",
    "Stay patient. Good things take time. ❤️",
    "Dream big, work hard, and never give up. 🔥",
    "Every day is a new chance to become better. 🌟",
]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Assalamu Alaikum! ❤️🔥\n\n"
        "Welcome to the Quotes Bot!\n\n"
        "Use /quote to get a motivational quote. ✨"
    )


async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    selected_quote = random.choice(QUOTES)
    await update.message.reply_text(
        f"✨ {selected_quote}"
    )


def main():
    token = os.getenv("BOT_TOKEN")

    if not token:
        raise ValueError("BOT_TOKEN environment variable is not set!")

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("quote", quote))

    print("Bot is running... 🚀")
    app.run_polling()


if __name__ == "__main__":
    main()
