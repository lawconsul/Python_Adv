import yaml
import json
import socket
import threading
import datetime
from argparse import ArgumentParser


# сформировать answer 2xx -сообщение;
def answer_2xx(code_error):
    return {
        'response': code_error,
        'time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'alert': ""
    }

# сформировать probe-сообщение;
def make_probe():
    return {
        'action': 'probe',
        'time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

def send(request):
    string_request = json.dumps(request)
    client.send(string_request.encode())
    bytes_response = client.recv(buffer_size)

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
    sock.bind((host, port))
    sock.listen(5)

    # Таймер каждые 2 сек должен отправлять сообщение, полученное от функции make_probe(), но делает это всего 1 раз
    t = threading.Timer(2.0, send, [make_probe()])
    t.start()

    while True: #event-loop
        client, (client_host, client_port) = sock.accept()
        print(f'Client {client_host}:{client_port} was connected' )

        bytes_request = client.recv(buffer_size)
        request = bytes_request.decode()
        print(f"Request: {request}")

        if request["action"] == "presence":
            send(answer_2xx('200'))
            client.send(bytes_request)
        # client.close()
