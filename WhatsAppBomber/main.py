from Classes import *
from Functions import *


def driver_bot():
    bot = WhatsappBot()
    bot.open_wpp()
    while True:
        bot.send_message()


# send_book()

sleep(5)
send_image()
