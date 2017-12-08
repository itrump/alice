import socket
import commands
import sys

""" when used for transfering files between local desktop and dev/online machines, 
        dev/online machines only works when they listen at port range between 8000-9000
    usage:
        This is a client/server mode file transform script.
        Run this script on the server side where files locate.
"""

################################# CONF 
HOST = '0.0.0.0'
PORT = 8876
BUFSIZE = 4096
################################# CONF 


ADDR = (HOST,PORT)

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv.bind(ADDR)
serv.listen(5)
serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

cmd = 'date'
status, output = commands.getstatusoutput(cmd)
print 'listening ... %s' % output

while True:
    try:
        conn, addr = serv.accept()
        status, dtime= commands.getstatusoutput(cmd)
        #print 'client connected ... %s, %s' % (addr, dtime)
        file_name = conn.recv(BUFSIZE)


        file_bytes = open(file_name, 'rb').read()
        total_len = len(file_bytes)
        #print 'file %s length %d bytes' % (file_name, total_len)
        conn.send(file_bytes)
        #print 'ok'
        conn.close()
        status, dtime= commands.getstatusoutput(cmd)
        print 'fisnished sending file %s, %s' % (file_name, dtime)

    except Exception, e:
        #print "exception caught:%s" % e
        break

