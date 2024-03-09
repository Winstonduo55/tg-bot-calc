from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import re

# Настройка логирования для вывода ошибок
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

logger = logging.getLogger(__name__)

# Функция для обработки команды /start
def start(update, context):
    update.message.reply_text('Привет! Я калькулятор. Просто отправь мне выражение для вычисления.')

# Функция для обработки текстовых сообщений с выражением для вычисления
def calculate(update, context):
    expression = update.message.text

    # Проверяем корректность выражения с помощью регулярного выражения
    if re.match(r'^[0-9+\-*/(). ]+$', expression):
        try:
            result = eval(expression)
            update.message.reply_text(f'Результат: {result}')
        except Exception as e:
            update.message.reply_text(f'Ошибка: {e}')
    else:
        update.message.reply_text('Ошибка: некорректное выражение.')

def main():
    # Создаем объект Updater и передаем в него токен вашего бота
    updater = Updater("YOUR_TELEGRAM_BOT_TOKEN", use_context=True)

    # Получаем диспетчер для регистрации обработчиков
    dp = updater.dispatcher

    # Регистрируем обработчик команды /start
    dp.add_handler(CommandHandler("start", start))

    # Регистрируем обработчик для текстовых сообщений
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, calculate))

    # Запускаем бота
    updater.start_polling()

    # Останавливаем бота при нажатии Ctrl+C
    updater.idle()

if __name__ == '__main__':
    main()
