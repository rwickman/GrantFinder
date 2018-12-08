# Test client for search
import socket

HOST = socket.gethostname()    # The remote host
PORT = 50001              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    toSend = input("Query: ")
    s.sendall(toSend.encode())
    
    print("SENT")
    while True:
        data = s.recv(1024)
        data_decoded = data.decode()
        print(data_decoded)
        if not data_decoded:
            break

print('Received', repr(data))