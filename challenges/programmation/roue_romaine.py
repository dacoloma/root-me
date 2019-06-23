import socket
import codecs

# Parameters
HOST = 'irc.root-me.org'
PORT = 6667
CHANNEL = '#root-me_challenge'
BOT = 'candy'
NICKNAME = 'Danonino'

# Open a socket 
IRC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connection to server
def irc_conn():
    IRC.connect((HOST, PORT))
    
# Send data
def send_data(command):
    IRC.send("{} \n".format(command).encode())

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
        #Start challenge
        send_data("PRIVMSG candy !ep3\r")
        
        #Receive bot response
        msg = IRC.recv(1024).decode('utf-8', 'ignore')
        print(msg)

        resp = msg.split(':')
        resp = resp[len(resp) - 1]
        print(resp)
        allo = codecs.decode(resp, 'rot_13')

        print(allo)
        send_data(f"PRIVMSG candy !ep3 -rep {allo} \r")

IRC.close()

print("Closing connection")