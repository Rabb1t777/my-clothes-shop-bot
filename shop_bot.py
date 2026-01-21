# shop_bot.py
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler

# === НАСТРОЙКИ — ЗАМЕНИТЕ НА СВОИ ===
BOT_TOKEN = "8063864783:AAEjiGP7SfYbIc5EHG8-J7drGFrTtELaF1g"        # ← Обязательно замените!
SHOP_URL = "https://funny-export-72093872.figma.site"         # ← Должен начинаться с https://

# =====================================

async def start(update, context):
    """Обработчик команды /start"""
    keyboard = [[InlineKeyboardButton("🛍 Открыть магазин", url=SHOP_URL)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Добро пожаловать в наш магазин одежды! 👗\n"
        "Нажмите кнопку ниже, чтобы начать покупки:",
        reply_markup=reply_markup
    )

async def help_command(update, context):
    """Обработчик команды /help"""
    await update.message.reply_text(
        "ℹ️ <b>Справка</b>\n\n"
        "Этот бот поможет вам быстро перейти в наш онлайн-магазин.\n\n"
        "<b>Команды:</b>\n"
        "/start — открыть магазин\n"
        "/help — показать эту справку",
        parse_mode="HTML"
    )

def main():
    """Запуск бота"""
    app = Application.builder().token(BOT_TOKEN).build()

    # Регистрация обработчиков
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("✅ Бот запущен. Нажмите Ctrl+C для остановки.")
    app.run_polling()

if __name__ == "__main__":
    main()