# import sys
import yaml
import json
import socket
from argparse import ArgumentParser
import datetime
import threading


def make_request(text):
    return {
        'data': text
    }


# сформировать presence-сообщение;
def make_presence():
    return {
        'action': 'presence',
        'time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'type': 'status',
        'user': {
            'account_name': session['account_name'],
            'status': session['status']
        }
    }

def send(request):
    # request = make_presence()
    string_request = json.dumps(request)
    sock.send(string_request.encode())
    bytes_response = sock.recv(buffer_size)


if __name__ == '__main__':
    config = {
        'host': 'localhost',
        'port': 8000,
        'buffer_size': 1024
    }
    parser = ArgumentParser()
    parser.add_argument('-c', '--config', type=str, required=False, help='Sets config path')
    parser.add_argument('-ht', '--host', type=str, required=False, help='Sets server host')
    parser.add_argument('-p', '--port', type=str, required=False, help='Sets server port')

    args = parser.parse_args()

    if args.config:
        with open(args.config) as file:
            file_config = yaml.safe_load(file)
            config.update(file_config or {})

    host = args.host if args.host in args else config.get('host')
    port = args.port if args.port in args else config.get('port')
    buffer_size = config.get('buffer_size')

    sock = socket.socket()
    sock.connect((host, port))

    # Словарь для хранения параметров текущей сессии пользователя
    session = {
        'account_name': 'guest',
        'password': 'qwerty',
        'status': 'present',
    }

    send(make_presence())

    # event-loop: make_request - 'Enter your message:'
    while True:
        message = input('Enter your message:')
        request = make_request(message)
        string_request = json.dumps(request)

        sock.send(string_request.encode())
        bytes_response = sock.recv(buffer_size)

        response = json.loads(bytes_response)
        # print(f'Send message to {host}:{port}')
        print(response)

        if request["action"] == "probe":
            send(make_presence())
        # sock.close()




# python client.py localhost 8000
# python client.py -c config.yml
