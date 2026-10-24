import os
import logging

from telegram import Update
from telegram.ext import (
Application,
CommandHandler,
MessageHandler,
ContextTypes,
filters,
)

logging.basicConfig(level=logging.INFO)
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
await update.message.reply_text(
"سلام! 👋\n"
"به NEXORA AI خوش اومدی! 🤖\n\n"
"پیامت رو بفرست تا دریافتش کنم."
)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
await update.message.reply_text(
"دستورات ربات:\n"
"/start - شروع ربات\n"
"/help - راهنما"
)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
text = update.message.text

await update.message.reply_text(
    f"پیامت دریافت شد! ✅\n\n"
    f"نوشتی:\n{text}\n\n"
    "هوش مصنوعی هنوز به این نسخه متصل نشده است. 🧠"
)

def main():
if not TOKEN:
raise RuntimeError(
"TELEGRAM_BOT_TOKEN تنظیم نشده است."
)

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
)

print("NEXORA AI is starting...")

app.run_polling()

if name == "main":
main()
