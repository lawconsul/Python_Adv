import yaml
import json
import socket
from argparse import ArgumentParser
import logging
from resolvers import find_server_action
from protocol import validate_request, make_200, make_500, make_400, make_404

import select
from handlers import handle_tcp_request
import threading

config = {
    'host': 'localhost',
    'port': 8000,
    'this_port': 8000,
    'buffersize': 1024,
}


parser = ArgumentParser()
parser.add_argument('-c', '--config', type=str, required=False,
                    help='Sets config path')
parser.add_argument('-ht', '--host', type=str, required=False,
                    help='Sets other host')
parser.add_argument('-p', '--port', type=str, required=False,
                    help='Sets other hosts port')
parser.add_argument('-p', '--this_port', type=str, required=False,
                    help='Sets this hosts port')

args = parser.parse_args()

if args.config:
    with open(args.config) as file:
        file_config = yaml.safe_load(file)
        config.update(file_config or {})

host = args.host if args.host else config.get('host')
port = args.port if args.port else config.get('port')
this_port = args.this_port if args.this_port else config.get('this_port')
buffersize = config.get('buffersize')


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=(
        logging.FileHandler('p2p_client.log'),
        logging.StreamHandler()
    )
)

requests = []
connections = []

def read(sock, requests, buffersize):
    bytes_request = sock.recv(buffersize)
    if bytes_request:
       requests.append(bytes_request)

def write(sock, response):
    sock.send(response)

try:
    sock = socket.socket()
    sock.bind((host, port))
    sock.setblocking(0)
    sock.listen(5)

    logging.info(f'p2p_client started with port={port}, connected to {host}:{port}')

    action_mapping = find_server_action()

    while True:
        try:
            client, (client_host, client_port) = sock.accept()
            logging.info(f'p2p_client {client_host}:{client_port} was connected')
            connections.append(client)
        except:
            pass

        rlist, wlist, xlist = select.select(
            connections, connections, connections, 0
        )

        for read_client in rlist:
            # bytes_request = read_client.recv(buffersize)
            # requests.append(bytes_request)
            read_thread = threading.Thread(target=read, args=(read_client, requests, buffersize))
            read_thread.start()

        if requests:
            bytes_request = requests.pop()
            bytes_response = handle_tcp_request(bytes_request, action_mapping)

            for write_client in wlist:
                # write_client.send(bytes_response)
                write_thread = threading.Thread(target=write, args=(write_client, bytes_response))
                write_thread.start()

except KeyboardInterrupt:
    logging.info('p2p_client shutdown')


