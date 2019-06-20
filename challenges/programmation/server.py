import socket 

def retour_au_college(entry):
    if len(entry) >= 3:
        val = entry[1].split('/')
        a = sqrt(int(val[0]))
        return (a * int(val[1]))

# Parameters
HOST = 'irc.root-me.org'
PORT = 6667
CHANNEL = '#root-me_challenge'
BOT = 'Candy'
NICKNAME = 'Danonino'

input('Opening socket')
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
    send_data('USER {} {} {} Daniel'.format(nickname, nickname, nickname))
    send_data("NICK {}".format(nickname))

# Join channel
def join(channel):
    send_data("JOIN {}".format(channel))

input('Connecting to host')
irc_conn()

input('Logging in')
login(NICKNAME)

input('Joining channel')
join(CHANNEL)

input('start')
send_data("PRIVMSG {} !ep1".format(CHANNEL))
option = ""
while option != "quit":
    msg = IRC.recv(1024).decode()

    if msg.find('PING') != -1:
        send_data("PONG {}".format(msg.split()[1]))
    print(msg)
    if "PRIVMSG" in msg and CHANNEL in msg:
        resp = retour_au_college(msg.split()[1])
        send_data("PRIVMSG {} !ep1 -rep {} ".format(CHANNEL, resp))
    option = (input("> "))
# while 1:


IRC.close()



print("Closing connection")
