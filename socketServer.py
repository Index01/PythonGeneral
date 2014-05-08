import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 9999))
s.listen(5)

print "TCPServer Waiting for client on port 9999"

while 1: 
    client, address = s.accept()
    print "[+]connected"
    data = client.recv(512)
    print data
    data = client.recv(512) + "some dumb response here" 
    if data: 
        client.send(data) 
    client.close()
