import smtplib as e_lib
from email.message import EmailMessage
from math import floor
from random import choice
from time import time

from Utils import get_url_text

# Get book's content
book_text = get_url_text("https://www.gutenberg.org/files/2600/2600-h/2600-h.htm")

# Split the words of each book into a list of words
word_list = book_text.split(" ")

# Determine the message size of each email, and then the size of the residual email
msg_size = floor(len(word_list) / 1000)
final_msg_size = len(word_list) - (msg_size * 999)
print(f"Words per message: {msg_size}\nFinal message size: {final_msg_size}")

# Sending variables
user_list = []
fr_address_list = []
password_list = []
recipient_mail_list = []
email_counter = [[0] for _ in range(len(recipient_mail_list))]

# E-mail lib variables
e_lib_host = 'smtp.gmail.com'
e_lib_port = 587

# Setup email variables
start_pos = msg_count = user_changer = 0
subject = 'WAR AND PEACE'
msg_text = ''

start_time = time()  # Time counter

# create and send email
for b in range(20):

    # Reset user if necessary
    if user_changer > len(user_list) - 1:
        user_changer = 0

    # User loop information
    user = user_list[user_changer]
    password = password_list[user_changer]
    fr_address = fr_address_list = user_changer

    # Open the email server connection
    server = e_lib.SMTP(host=e_lib_host, port=e_lib_port)
    server.starttls()
    server.login(user=user, password=password)

    # Create and send the message
    for i in range(50):

        to_address = choice(recipient_mail_list)  # Random recipient

        # Recipient counter
        for cont in range(len(email_counter)):
            if cont == recipient_mail_list.index(to_address):
                email_counter[cont][0] += 1
        for name in recipient_mail_list:
            split_name = name.split('@')
            print(f'Nome: {split_name[0]} || Envios: {email_counter[recipient_mail_list.index(name)][0]}  #  ', end='')

        # Check to see if this is the final message, which has a slightly different range
        if msg_count == 1000:
            start_pos = (len(word_list) - final_msg_size)
            msg_text = ' '.join(word_list[start_pos:])
        else:
            start_pos = msg_count * msg_size
            msg_text = ' '.join(word_list[start_pos:start_pos + msg_size])

        # Create the email message headers and set the payload
        msg = EmailMessage()
        msg['From'] = fr_address
        msg['To'] = to_address
        msg['Subject'] = subject + str(msg_count + 1)
        msg.set_payload(msg_text)

        # Control variables
        msg_count += 1
        print(f'{user}  #  ')
        print(f'{time() - start_time} seconds')

        # Open the email server and send the message
        server.send_message(msg)

    # Delay each batch by 60 seconds to avoid sending limits ~~ I don't know if that's really necessary
    user_changer += 1
    server.close()
