import socket
import time
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 9999))
data = "knock knock"
confirm = "1"

print "[+]CONNECTING..."
client.send(data)

data = "acknowledgement: " + client.recv(512)  
print data 
