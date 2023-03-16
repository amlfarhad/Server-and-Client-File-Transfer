import socket
from concurrent.futures import ThreadPoolExecutor

TCP_IP = socket.gethostbyaddr("3.129.88.101")[0]
TCP_PORT = 9001
BUFFER_SIZE = 1024
FILE_NAME = 'mytext.txt'

print('TCP_IP=',TCP_IP)
print('TCP_PORT=',TCP_PORT)

def send_file(conn):
    with open(FILE_NAME, 'rb') as f:
        while True:
            l = f.read(BUFFER_SIZE)
            if not l:
                break
            conn.sendall(l)
    conn.close()

def handle_client(conn, addr):
    print('Got connection from', addr)
    try:
        send_file(conn)
    except Exception as e:
        print('Error:', e)

def main():
    with ThreadPoolExecutor(max_workers=5) as executor:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcpsock:
            tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            tcpsock.bind((TCP_IP, TCP_PORT))
            tcpsock.listen(5)
            print('Waiting for incoming connections...')
            while True:
                conn, addr = tcpsock.accept()
                executor.submit(handle_client, conn, addr)

if __name__ == '__main__':
    main()
