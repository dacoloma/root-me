import socket 

def backtocollege(entry):
    if len(entry) >= 3:
        val = entry[1].split('/')
        a = sqrt(int(val[0]))
        return (a * int(val[1]))

# Parameters
HOST = 'irc.root-me.org'
PORT = 6667
CHANNEL = '#root-me_challenge'
BOT = 'candy'
NICKNAME = 'Danonino'

# input('Opening socket')
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

# input('Connecting to host')
irc_conn()

# input('Logging in')
login(NICKNAME)

# input('Joining channel')
join(CHANNEL)

input('start')

option = ""
while option != "quit":
    msg = IRC.recv(1024).decode()
    # if "PRIVMSG" in msg and CHANNEL in msg:
    print(msg)

    if msg.find('PING') != -1:
        send_data("PONG {}".format(msg.split()[1]))
    
    option = input("Press Enter or type start or type quit: ")
    if option == "start":
        print("PRIVMSG candy !ep1\n".format(NICKNAME,BOT))
        input("> ")
        send_data("PRIVMSG candy !ep1\r".format(NICKNAME, BOT))
        input("> ")
        msg = IRC.recv(1024).decode()
        if "PRIVMSG" in msg and CHANNEL in msg:
            resp = backtocollege(msg.split()[1])
            print("Response: {}".format(resp))
            send_data("PRIVMSG candy !ep1 -rep {} \r".format(resp))



IRC.close()

print("Closing connection")
