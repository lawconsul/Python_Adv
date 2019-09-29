import yaml
import json
import zlib
import socket
from datetime import datetime
from argparse import ArgumentParser
import threading

# READ_MODE = 'r'
# WRITE_MODE = 'w'


def make_request(action, text, date=datetime.now()):
    return {
        'action': action,
        'data': text,
        'time': date.timestamp()
    }

def read(sock, buffersize):
    while True:
        compressed_response = sock.recv(buffersize)
        bytes_response = zlib.decompress(compressed_response)
        response = json.loads(bytes_response)
        print(response)


if __name__ == '__main__':
    config = {
        'host': 'localhost',
        'port': 8000,
        'buffersize': 1024,
    }

    parser = ArgumentParser()
    parser.add_argument('-c', '--config', type=str, required=False,
                        help='Sets config path')
    parser.add_argument('-ht', '--host', type=str, required=False,
                        help='Sets server host')
    parser.add_argument('-p', '--port', type=str, required=False,
                        help='Sets server port')
    # parser.add_argument('-m', '--mode', type=str, default=READ_MODE,
    #                     help='Sets server port')

    args = parser.parse_args()

    if args.config:
        with open(args.config) as file:
            file_config = yaml.safe_load(file)
            config.update(file_config or {})

    host = args.host if args.host else config.get('host')
    port = args.port if args.port else config.get('port')
    buffersize = config.get('buffersize')

    try:
        sock = socket.socket()
        sock.connect((host, port))

        read_thread = threading.Thread(target=read, args=(sock, buffersize))
        read_thread.start()

        while True:
            # if args.mode == WRITE_MODE:
            action = input('Enter action name: ')
            message = input('Enter your message: ')

            request = make_request(action, message)
            string_request = json.dumps(request)
            bytes_request = string_request.encode()
            compressed_request = zlib.compress(bytes_request)
            sock.send(compressed_request)
            # else:
                # compressed_response = sock.recv(buffersize)
                # bytes_response = zlib.decompress(compressed_response)
                # response = json.loads(bytes_response)
                # print(compressed_response)
                # print(response)
    except KeyboardInterrupt:
        print('Client shoutdown')
