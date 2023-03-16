import socket
import time

TCP_IP = '3.17.58.185' #(Example)
TCP_Port = 9001
BUFFER_SIZE = 1024
FILE_NAME = 'received_file'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_Port))

clock_start = time.monotonic()
with open(FILE_NAME, 'wb') as f:
    print('file opened')
    while True:
        data = bytearray(BUFFER_SIZE)
        size = s.recv_into(data)
        if not size:
            break
        f.write(data[:size])
    print('file closed')

s.close()
print('connection closed')

clock_end = time.monotonic()
duration_clock = clock_end - clock_start
print('duration_clock:', duration_clock)
