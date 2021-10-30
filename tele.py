from telebot import TeleBot

bot = TeleBot(__name__)
token = '2062148897:AAGkO4tdtzOhRw_MWolbaPX65C0XpcFJdcc'

@bot.route("/config")
def menu(msg):
  chat = msg['chat']['id']
  text = open('config.txt', 'r')
  bot.send_message(chat,text)
  
print("Bot RUN....")
if __name__ == '__main__':
  bot.config['api_key'] = token
  bot.poll(debug=True)