import socket 
from math import sqrt

def retour_au_college(arr):
    if len(arr) >= 2:
        val = arr[1].split('/')
        a = sqrt(int(val[0]))
        return (a * int(val[1]))

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(('irc.root-me.org', 6667))