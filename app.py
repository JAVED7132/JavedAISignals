
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """
🤖 Welcome to Javed AI Signals

Available Commands:

/start - Start Bot
/signal - Get AI Signal
/help - Help Menu
"""

    await update.message.reply_text(text)

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 AI Signal\n\n"
        "Pair: XAU/USD\n"
        "Signal: BUY 🟢\n"
        "Entry: 3350\n"
        "Take Profit: 3370\n"
        "Stop Loss: 3335"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Use:\n"
        "/start\n"
        "/signal\n"
        "/help"
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("signal", signal))
app.add_handler(CommandHandler("help", help_command))

app.run_polling()
