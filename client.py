import select
import socket
import sys

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(("localhost", 5555))
data = my_socket.recv(1024)

print "received: \n%s" % data

userinput = sys.stdin.readline()
outputs = []
my_socket.sendall(userinput)



my_socket.close()