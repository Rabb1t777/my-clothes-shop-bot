# shop_bot.py
import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler

# === НАСТРОЙКИ ===
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("Ошибка: переменная BOT_TOKEN не задана!")

SHOP_URL = "https://funny-export-72093872.figma.site"  # ← замените на ваш HTTPS-сайт

async def start(update, context):
    keyboard = [[InlineKeyboardButton("🛍 Открыть магазин", url=SHOP_URL)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Добро пожаловать в наш магазин одежды! 👗\n"
        "Нажмите кнопку ниже, чтобы начать покупки:",
        reply_markup=reply_markup
    )

async def help_command(update, context):
    await update.message.reply_text(
        "ℹ️ <b>Справка</b>\n\n"
        "Этот бот поможет вам быстро перейти в наш онлайн-магазин.\n\n"
        "<b>Команды:</b>\n"
        "/start — открыть магазин\n"
        "/help — показать эту справку",
        parse_mode="HTML"
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    print("✅ Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()

