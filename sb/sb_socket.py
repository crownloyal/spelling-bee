import socket
import pickle
import config

class SocketClientMixin:
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to_socketserver(self):
        self.socket.connect((config.server_host, config.socket_port))

    def receive_message_test(self):
        message = self.socket.recv(config.socket_message_buffer_length)
        print(message.decode("utf-8"))  
        self.socket.close()

    def send_message_test(self):
        message = ("Hello world!").encode("utf-8")
        self.socket.send(message)
        self.socket.close()

    def sock_send_object(self, obj):
        try:
            self.connect_to_socketserver()
            message = pickle.dumps(obj)
            message_header = f"{len(message):<{config.socket_message_header_length}}"
            composed = bytes(f"{message_header}", 'utf-8') + message
            self.socket.send(composed)
            self.socket.close()
        except Exception as ex:
            print(ex)

class SocketServerMixin:
    # socket.AF_INET - address family, IPv4, some otehr possible are AF_INET6, AF_BLUETOOTH, AF_UNIX
    # socket.SOCK_STREAM - TCP, conection-based, socket.SOCK_DGRAM - UDP, connectionless, datagrams, socket.SOCK_RAW - raw IP packets
    # self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # SO_ - socket option
    # SOL_ - socket option level
    # Sets REUSEADDR (as a socket option) to 1 on socket
    socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    sockets_active = [ socket_server ]
    clients_active = {}

    def __init__(self):
        self.socket_server.bind((config.server_host, config.socket_port))
        self.socket_server.listen(16)
        print(f'INFO: Listening for connections on {config.server_host}:{config.socket_port}')        

    def sendMessageTest(self, c_socket):
        while True:
            c_socket.send(bytes("Hey there!!!","utf-8"))

    def listen(self):
        clientsocket, address = self.socket_server.accept()
        print(f"INFO: Connection from {address} has been established")
        self.clients_active[address] = clientsocket

    def sock_receive_message(self, c_socket: socket.socket):
        full_message = b''
        new_message_flag = True

        while True: 
            bytes_data = c_socket.recv(config.socket_message_buffer_length)

            if bytes_data == '':
                # Escape if socket sends closing signal
                new_message_flag = True
                break
            
            if new_message_flag == True:
                print(f"INFO: New message queued for {c_socket}")
                modulate = bytes_data[:config.socket_message_header_length].decode("utf-8")
                message_length = int(modulate)
                new_message_flag = False

            print(f"INFO: Bytes received: {(len(full_message) - config.socket_message_header_length)}, expected: {message_length}")         

            if (len(full_message) - config.socket_message_header_length) == message_length:
                # Escape if message length equals expected byte payload
                break
            
            full_message += bytes_data

        object = pickle.loads(full_message[config.socket_message_header_length:])
        return object
            
            

    