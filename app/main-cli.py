import sys
from client import Client

if __name__ == '__main__':
    endpoint = 'http://localhost/tpmj'
    username = None if not sys.argv else sys.argv[0]
    client = Client(endpoint, username)
    accepted = client.run()
