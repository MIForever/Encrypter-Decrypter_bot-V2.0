import telebot
from telebot import types
from functions import encrypter,decrypter


token = 'TOKEN'
link ='LINK TO YOUR BOT'

bot = telebot.TeleBot(token)


#for command "start"
@bot.message_handler(commands=['start'])
def send_welcome(message):

    with open("members.txt", "a") as myfile:
        if(not str(message.chat.id) in str(open("members.txt", "r").read())):
            bot.send_message(message.from_user.id,"If you did not follow to 'YOUR CHANNEL'S USERNAME', please follow and send /start command again")
            myfile.write(str(message.chat.id)+",")
    bot.send_message(message.from_user.id,f'Hi {message.from_user.first_name}👋')
    #buttons
    global markup
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
    markup.row('Message to cipher')
    markup.row('Cipher to message')
    bot.send_message(message.from_user.id,'Choose one:👇',reply_markup=markup)


#for command "help"
@bot.message_handler(commands=['help'])
def help(message):
    textmessage = "After giving /start command, please choose one of 2 buttons. Next send message or cipher. Write with LATIN alphabet letters only. DON'T SEND EMOJIS!❌😃"
    bot.reply_to(message,textmessage)
    bot.send_message(message.from_user.id,"In order to start please press /start command")

#for command "share"
@bot.message_handler(commands=['share'])
def sharing(message):
    mrkp=types.InlineKeyboardMarkup()
    message_button = types.InlineKeyboardButton(text="Encrypter-decrypter bot",url=link)
    mrkp.add(message_button)
    bot.send_message(message.from_user.id,'Encrypter-decrypter bot is the bot that encryptes and decryptes your messages to make it secure🔓.',reply_markup=mrkp)

@bot.message_handler(commands=['users'])
def users_quantity(message):
    bot.send_message(message.from_user.id,"Members 👤: "+str(len(str(open("members.txt", "r").read()).split(","))-1))

#for messages
@bot.message_handler(content_types=['text'])
def choice(message):
    #cheking message
    if message.text == 'Message to cipher':
        markup = telebot.types.ReplyKeyboardRemove(selective=False)
        bot.reply_to(message,'Please send message...')
        bot.register_next_step_handler(message,convertor1)
    elif message.text=='Cipher to message':
        markup = telebot.types.ReplyKeyboardRemove(selective=False)
        bot.reply_to(message,'Please send cipher...')
        bot.register_next_step_handler(message,convertor2)
    else:
        bot.send_message(message.from_user.id,"I don't know how to respond🤷‍♂️")

#converting to code
def convertor1(message):
    global wordtocipher
    wordtocipher = message.text
    bot.reply_to(message,'Please send password...')
    bot.register_next_step_handler(message,get_password)
    
#converting to message
def convertor2(message):
    global ciphertoword
    ciphertoword = message.text
    bot.reply_to(message,'Please send password...')
    bot.register_next_step_handler(message,get_password2)
    
def get_password(password):
    if password.text.isdigit():
        code = encrypter(message=wordtocipher,password=password.text)
        bot.reply_to(password,f"Cipher:")
        bot.send_message(password.from_user.id,code)
    else:
        bot.reply_to(password,"Password must be digital!")

def get_password2(password):
    if password.text.isdigit():
        secret_message = decrypter(cipher=ciphertoword,password=password.text)
        bot.reply_to(password,f"Message:")
        bot.send_message(password.from_user.id,secret_message)
    else:
        bot.reply_to(password,"Password must be digital!")


bot.polling(none_stop=True)