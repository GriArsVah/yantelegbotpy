# Подгружаем библиотеку бота
import telebot

# Иницируем экземляр класса
bot = telebot.TeleBot('5833797099:AAG4wB1WWpvSHsUXWldJUF6SFfm0mqydF2o')

# Запуск декоратора "message_handler" и декорируемую функцию "mes"
@bot.message_handler(content_types=['text'])
def mes(message):
    bot.send_message(message.chat.id, message.text)

# Запускаем
bot.polling(none_stop=True)