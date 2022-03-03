import  socket
sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
sock.connect(('localhost', 5555))
while True:
    name = input(">")

    if name == "":
        sock.close()
        break
    else:
        sock.send(name.encode())