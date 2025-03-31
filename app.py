import telebot  

# استبدل التوكن ده بتوكن البوت بتاعك
TOKEN = "7792326580:AAF1Gt3KFsSrZZ-y_m08SQ8yL1uSi_9T0DI"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بيك! البوت شغال 🎉")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling() 
