import socket
import codecs

# Parameters
HOST = 'irc.root-me.org'
PORT = 6667
CHANNEL = '#root-me_challenge'
BOT = 'candy'
NICKNAME = 'Danoninobot'

# Open a socket 
IRC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connection to server
def irc_conn():
    IRC.connect((HOST, PORT))
    
# Send data
def send_data(command):
    print("{} \n".format(command).encode().replace(b'\r\n', b''))
    IRC.send("{} \n".format(command).encode().replace(b'\r\n', b''))

# Login
def login(nickname):
    send_data(f"USER {nickname} {nickname} {nickname} Daniel")
    send_data(f"NICK {nickname}")

# Join channel
def join(channel):
    send_data(f"JOIN {channel}")

# input('Connecting to host')
irc_conn()

# input('Logging in')
login(NICKNAME)

# input('Joining channel')
join(CHANNEL)

input('start')

option = ""
while option != "quit":
    msg = IRC.recv(1024).decode('utf-8', 'ignore')
    print(msg)
    if msg.find('PING') != -1:
        send_data(f"PONG {msg.split()[1]}")
    
    option = input("Press Enter or type start or type quit: ")
    if option == "start":
        send_data(f"PRIVMSG {BOT} !ep3")
        msg = IRC.recv(1024).decode('utf-8', 'ignore')
        print(msg)
        resp = msg.split(":")
        resp = resp[-1]
        decode = codecs.decode(resp, "rot13")
        print(f"RESP : {resp.encode()} |")
        print(f"DECODE : {decode.encode()} |")
        # option = input("type quit: ")
        send_data(f"PRIVMSG {BOT} !ep3 -rep {decode}")

IRC.close()

print("Closing connection")