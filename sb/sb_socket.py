import socket
import pickle
import config

class SocketClientMixin:
    # socket.AF_INET - address family, IPv4, some other possible are AF_INET6, AF_BLUETOOTH, AF_UNIX
    # socket.SOCK_STREAM - TCP, connection-based, socket.SOCK_DGRAM - UDP, connectionless, datagrams, socket.SOCK_RAW - raw IP packets
    # self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to_socketserver(self):
        # https://docs.python.org/3/howto/sockets.html
        # send() returns zero if broken
        try:
            self.socket.send("".encode("utf-8")) == 0
        except:
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.connect((config.server_host, config.socket_port))

    def close_socket(self):
        try:
            if self.socket.send("".encode("utf-8")) != 0:
                self.socket.close()
        except:
            pass

    def receive_message_test(self):
        message = self.socket.recv(config.socket_message_buffer_length)
        print(message.decode("utf-8"))  

    def send_message_test(self):
        message = ("Hello world!").encode("utf-8")
        self.socket.send(message)

    def sock_send_object(self, obj):
        try:
            self.connect_to_socketserver()
            message = pickle.dumps(obj)
            message_header = f"{len(message):<{config.socket_message_header_length}}"
            composed = bytes(f"{message_header}", 'utf-8') + message
            self.socket.send(composed)
        except Exception as ex:
            print(ex)

class SocketServerMixin(SocketClientMixin):
    
    def __init__(self):
        super()
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # SO_ - socket option
        # SOL_ - socket option level
        # Sets REUSEADDR (as a socket option) to 1 on socket
        self.socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket_server.bind((config.server_host, config.socket_port))
        self.socket_server.listen(16)
        print(f'INFO: Listening for connections on {config.server_host}:{config.socket_port}')
        self.sockets_active = [ self.socket_server ]
        self.clients_active = {}

    def listen(self):
        clientsocket, address = self.socket_server.accept()
        print(f"INFO: Connection from {address} has been established")

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
            
            

    