import select
import socket
MAX_MSG_LENGTH = 1024
SERVER_PORT = 5555
SERVER_IP = "0.0.0.0"
print("loading......")
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen()
print("ready")
client_sockets = []
while True:
    rlist, wlist, xlist = select.select([server_socket] + client_sockets, [], [])
    for current_socket in rlist:
        if current_socket is server_socket:
            connection, client_address = current_socket.accept()
            print("New client joined!", client_address)
            client_sockets.append(connection)
        else:
            print("Data from existing client\n")
            data = current_socket.recv(MAX_MSG_LENGTH).decode()
            if data == "":
                print("new friend here ")
                client_sockets.remove(current_socket)
                current_socket.close()
            else:
                print(data)
                for i in client_sockets:
                    i.send(data.encode())
