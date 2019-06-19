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

# Open a socket 
IRC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connection to server
def irc_conn():
    IRC.connect((HOST, PORT))
    
# Send data
def send_data(command):
    IRC.send(command + '\n').encode()

# Login
def login(nickname):
    send_data("USER %s %s %s %s" % nickname nickname nickname "Daniel")
    send_data("NICK %s" % nickname)

# Join channel
def join(channel):
    send_data("JOIN %s" % channel)

def get_msg():
    msg = IRC.recv(1024)
    if (msg.find('PING') != -1):
        send_data('PONG %s' % msg.split()[1])
    return msg

irc_conn()
login(NICKNAME)
join(CHANNEL)

while 1:
    msg = IRC.recv(1024)
    print(msg)
IRC.close()



print("Closing connection")
