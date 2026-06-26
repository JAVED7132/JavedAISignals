
import os
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_KEY = os.getenv("TWELVE_API_KEY")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Welcome to Javed AI Signals\n\n"
        "Commands:\n"
        "/signal - Live Gold Signal\n"
        "/help - Help"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start\n"
        "/signal\n"
        "/help"
    )

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = f"https://api.twelvedata.com/price?symbol=XAU/USD&apikey={API_KEY}"

    try:
        r = requests.get(url, timeout=10)
        data = r.json()

        if "price" not in data:
            await update.message.reply_text("❌ Live price not available.")
            return

        price = float(data["price"])

        direction = "BUY 🟢" if int(price) % 2 == 0 else "SELL 🔴"

        if "BUY" in direction:
            tp = round(price + 20, 2)
            sl = round(price - 15, 2)
        else:
            tp = round(price - 20, 2)
            sl = round(price + 15, 2)

        text = (
            "📊 AI Gold Signal\n\n"
            f"Pair: XAU/USD\n"
            f"Signal: {direction}\n"
            f"Entry: {price}\n"
            f"Take Profit: {tp}\n"
            f"Stop Loss: {sl}"
        )

        await update.message.reply_text(text)

    except Exception as e:
        await update.message.reply_text(f"Error: {e}")

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("signal", signal))

if __name__ == "__main__":
    app.run_polling()

