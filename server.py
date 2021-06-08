import socket
import threading
import os


HEADER = 64
PORT = 12345
FORMAT = 'ascii'

#SERVER = str(socket.gethostbyname(socket.gethostname()))
SERVER = '127.0.0.1'
ADDR = (SERVER,PORT)
server= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('[SERVER]: Starting Server...')
server.bind(ADDR)

def start_server():
    print('waiting for connections..')
    server.listen()
    
    while True:
        conn,addr = server.accept()
        t = threading.Thread(target=connect,args=(conn,addr))
        t.start()
        print(f'[CONNECTIONS COUNT]: {threading.activeCount()-1} ')


def files_str_len(files):
    l=0
    for f in files:
        l += len(f)
    return l


def files_str(files):
    s =''
    for f in files:
        s+=f+'\n'
    
    return s



def connect(conn,addr):
    print(f'connection established with {addr}')
    files = os.listdir('server\\')

    #sending header for msg length
    msg = files_str(files)
    msg_len = str(len(msg))
    msg_len += ' '* (HEADER - len(files))
    print('sent msg len ',len(msg_len))
    # sending message length
    conn.send(bytes(msg_len,FORMAT))
    # sending real message
    conn.send(bytes(msg,FORMAT))
     
    file_name_len = conn.recv(HEADER).decode(FORMAT)
    if file_name_len:
        file_name_len = int(file_name_len)
        filename = conn.recv(file_name_len).decode(FORMAT)
        print('file requested for download',filename)

    
    


start_server()






'''
print('START')
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',12345))
s.listen(5)

print('listening to clients ...')
conn,addr = s.accept()
print('connected to client of address',addr)


f = open('server\data.txt','rb')

data = f.read(1024)
while data:    
    #print(data)
    conn.send(data)
    data = f.read(1024)
try:
    s.shutdown(1)
except OSError:
    print('connection closed....')
    s.close()
print('shut down..........')

#msg = s.recv(1024)
#print('message from client:',msg)
'''    