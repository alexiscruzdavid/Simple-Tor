from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from typing import List, Tuple
import socket
import relay_directory
import ssl
import time
import start_tor as tor
import sys
import os

UPLOAD_INTERVAL = 60
DOWNLOAD_INTERVAL = 60

class OnionRelay:
    def __init__(self, ip: str, port:int):
        self.ip = ip
        self.port = port
        self.connections = {}
        self.circuits = {}
        self.onion_key = None
        self.long_term_key = None
        self.server_socket = None

        self.create_keys()
        self.create_socket()
        self.upload_state()
        self.update_connections()

    def create_keys(self):
        # Make actual certs and keys and stuff
        self.onion_key = os.urandom(32)
        self.long_term_key = os.urandom(32)

    def create_socket(self):
        server_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        server_context.load_cert_chain(certfile, keyfile)

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.ip, self.port))
        self.server_socket.listen(tor.MAX_RELAYS + tor.MAX_CLIENTS)

        print('Onion Relay listening at {}:{}'.format(self.ip, self.port))

    def upload_state(self):
        '''
        Upload relay state to directory server
        '''
        while True:
            # TODO: upload state to directory server
            time.sleep(UPLOAD_INTERVAL)

    def download_states(self) -> Tuple[str, int]:
        '''
        Get states from directory server and update connections/states to relays
        '''
    #   Get actual states


    def update_connections(self) -> None:
        '''
        Update tls connections to relays
        '''
        while True:
            relays = self.download_states()
            time.sleep(DOWNLOAD_INTERVAL)


    def create_circuit(self):
        pass

    def extend_circuit(self):
        pass

    def destroy_circuit(self):
        pass


    def __str__(self):
        return 'IP: {}:{} /nOnion Key: {} /nConnections :{}'.format(self.ip, self.port, self.onion_key, self.connections)




def open_tls_connection(src_ip, dest_ip, certfile, keyfile):
    server_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    # the long term identiy key is the keyfile
    server_context.load_cert_chain(certfile, keyfile)

    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind((src_ip, 8443))
    server_sock.listen(5)

    print('Onion Proxy listening on port 8443...')

    while True:
        client_sock, client_addr = server_sock.accept()
        print('Received connection from {}'.format(client_addr))

        tls_server_sock = server_context.wrap_socket(client_sock, server_side=True)