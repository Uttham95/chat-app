import socket
import random
from threading import Thread
from datetime import datetime
from colorama import Fore, init, Back

# init colors
init()

# set the available colors
colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW]

# choose a random color for the client
client_color = random.choice(colors)

# server's IP address if the server is not on this machine, put the private (network) IP address (e.g 192.168.1.2)
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5002 # server's port
separator_token = "<SEP>" # we will use this to separate the client name & message

# initialize socket
s = socket.socket()
print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
# connect to the server
s.connect((SERVER_HOST, SERVER_PORT))
print("[+] Connected.")
# prompt the client for a name
name = input("Enter your name: ")

#keep listening to messages from server and print them123
def listen_for_messages():
    while True:
        message = s.recv(1024).decode()
        print("\n" + message)

# make a thread that listens for messages to this client & print them
t = Thread(target=listen_for_messages)
t.daemon = True
t.start()

while True:
    # input message we want to send to the server
    to_send =  input()
    # a way to exit the program
    if to_send.lower() == 'q':
        break
    # add the datetime, name & the color of the sender
    date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
    to_send = f"{client_color}[{date_now}] {name}{separator_token}{to_send}{Fore.RESET}"
    #send the message
    s.send(to_send.encode())

# close the socket
s.close()