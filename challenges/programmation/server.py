import socket 

HOST = ''
PORT = 12800
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind((HOST, PORT))
conn.listen(5)
print("Le serveur écoute à présent sur le port {}".format(PORT))
conn_client, infos_conn = conn.accept()
msg_recv = b""

while msg_recv != b"fin":
    msg_recv = conn_client.recv(1024)
    print(msg_recv.decode())
    conn_client.send(b"5/5")

print("Closing connection")
conn_client.close()
conn.close()