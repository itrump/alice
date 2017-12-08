import socket
import sys
import commands

#
#  usage :
#     python script remote/path/to/file local/path/to/file
#

#HOST = '10.99.22.39'
#HOST = '10.99.39.52'
#HOST = '10.99.39.52'
#HOST = '10.23.17.40'
#HOST = '172.18.19.35'
#HOST = '10.99.39.57'
#HOST = '10.94.208.31'
HOST = '10.145.85.70'
PORT = 8876
ADDR = (HOST,PORT)
# 8M
BUFSIZE = 1024 * 1024 * 32

# here conf a full path file like path/to/file/name
#file = /tmp/head.5000.router.log
if (len(sys.argv) < 3):
    print 'please spec file to transfer, file to write.'
    exit()

#file = /tmp/client.py
remote_file_name = sys.argv[1]
local_file_name = sys.argv[2]

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# send server the file to get

try:
    client.connect(ADDR)
    client.send(remote_file_name)
    cmd = 'date'

    status, dtime= commands.getstatusoutput(cmd)
    print 'client %s send %s... , %s' % (client, remote_file_name, dtime)

    myfile = open(local_file_name, 'wb')
    recv_len = 0
    while True:
      data = client.recv(BUFSIZE)
      if not data: break
      myfile.write(data)
      dlen = len(data)
      recv_len += dlen
      status, dtime= commands.getstatusoutput(cmd)
      print 'writing file .... %s, recv %d, total recv length:%d '               % (dtime, dlen, recv_len)

    myfile.close()
    status, dtime= commands.getstatusoutput(cmd)
    print 'finished writing file %s ' % (dtime)
    client.close()
    status, dtime= commands.getstatusoutput(cmd)
    print 'client disconnected %s' % (dtime)
    print 'receive %s success, exit' % local_file_name

except Exception as e:
    print "exception caught:%s" % e
