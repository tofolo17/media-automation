from Classes import *


def main():
    message = input()
    recipient = input()

    bot = WhatsappBot(message, recipient)
    bot.open_wpp()
    while True:
        bot.send_message()


main()
