import socket
import threading
import os


HEADER = 64
PORT = 12345
FORMAT = 'utf-8'
DISCONNECT = 'DISCONNECT'


#SERVER = str(socket.gethostbyname(socket.gethostname()))
#SERVER = '127.0.0.1'
#SERVER = '119.160.97.67'
SERVER = ''
ADDR = (SERVER,PORT)
server= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('[SERVER]: Starting Server...')
server.bind(ADDR)

def start_server():
    print('Server address : ',ADDR)
    print(print(FORMAT))
    server.listen()
    
    print('waiting for connections..')
    while True:
        conn,addr = server.accept()
        try:
            t = threading.Thread(target=send_file_menu,args=(conn,addr))
            t.start()
            print(f'[ CONNECTION ESTABLISHED ]: {addr} connected with server.')
            print(f'[CONNECTIONS COUNT]: {threading.activeCount()-1} ')
        except:
            print('[ EXCEPTION ] : Exception occured while establishing connection.')

#
def files_str(files):
    s =''
    for f in files:
        s+=f+'\n'
    
    return s



def send_file(conn,addr,path):
    print(f'[ FILE TRANSFER ] {addr} requested for file "{path}" ')
    f = open(f'server\{path}','r')
    file = f.read()
    file_len = str(len(file))
    file_len += ' '* (HEADER - len(file_len))
    print('[ STATUS ] : sending file...')
    #print(file)
    print('\n',len(file))
    
    # sending file length as header
    conn.send(bytes(file_len,FORMAT))
    # sending complete file
    conn.send(bytes(file,FORMAT))
    print(f'[ COMPLETED ] : file "{path}" sent successfully to {addr}.')



def send_file_menu(conn,addr):
    files = os.listdir('server\\')
    #sending header for msg length
    msg = files_str(files)
    send(msg,conn)
    filename = recv(conn)
    if filename:
        send_file(conn,addr,filename)
    msg = recv(conn)
    if msg ==DISCONNECT:
        conn.close()
        print(f'[CLOSED]: Connection with {addr} closed.')
    print(f'[CONNECTIONS COUNT]: {threading.activeCount()-1} ')
        

    
# for sending messages to clients    
def send(msg,conn):
    msg_len = str(len(msg))
    msg_len += ' '* (HEADER - len(msg))
    # sending message length
    conn.send(bytes(msg_len,FORMAT))
    # sending real message
    conn.send(bytes(msg,FORMAT))
    

# for receiving messages from clients
def recv(conn):
    msg_len = conn.recv(HEADER).decode(FORMAT)
    if msg_len:
        msg = conn.recv(int(msg_len)).decode(FORMAT)
        return msg


start_server()




