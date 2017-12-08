import socket
import sys

HOST = '10.99.39.57'
PORT = 8876
ADDR = (HOST,PORT)
BUFSIZE = 4096

if (len(sys.argv) < 2):
    print "pls spec file 2b transfered."
    exit()

file_name = sys.argv[1]

bytes = open(file_name).read()

print len(bytes)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

client.send(bytes)

client.close()
