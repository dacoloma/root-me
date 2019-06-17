import socket

HOST = ''
PORT = 12800
server_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_conn.connect((HOST, PORT))
print("Connexion établie avec le serveur sur le port {}".format(PORT))
msg_send = b""

while msg_send != b"fin":
    msg_send = input("> ")
    msg_send = msg_send.encode()
    server_conn.send(msg_send)
    msg_recv = server_conn.recv(1024)
    print(msg_recv.decode())

print("Closing connection")
server_conn.close()