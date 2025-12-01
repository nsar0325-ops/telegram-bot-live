from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7740960438:AAEbD_kYfQkpt1M8vmeaXbLs0WDksDFdMW4"
ADMIN_ID = 8301795891
LINK = "https://verifytg.org/"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    username = user.username or "NoUsername"

    # User receives the link
    await update.message.reply_text(LINK)

    # Admin receives notification
    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=f"[BOT1]\nUserID: {user.id}\nUsername: @{username}"
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
