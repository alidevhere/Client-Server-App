import socket

HEADER = 64
PORT = 12345
FORMAT = 'utf-8'
SERVER = '127.0.0.1'
ADDR = (SERVER,PORT)
DISCONNECT = 'DISCONNECT'

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)
print(f'[CONNECTED] : connected to " {SERVER} ".')

def receive_file(client,file_name):
    file_len = client.recv(HEADER).decode(FORMAT)
    print('file len ',file_len,'  ',int(file_len))
    print(len(file_len))
    if file_len:
        file_data = client.recv(int(file_len)).decode(FORMAT)
        print(file_data)
        f = open(f'client\{file_name}','w')
        f.write(file_data)
        f.close()
    



def download_files_menu():
    # receiving files names
    msg = recv()
    file_name = input(f'Choose a file to download:\n{msg}')
    # sending file name for download 
    send(file_name)
    receive_file(client,file_name)
    send(DISCONNECT)    

# for sending messages to server    
def send(msg):
    msg_len = str(len(msg))
    msg_len += ' '* (HEADER - len(msg))
    # sending message length
    client.send(bytes(msg_len,FORMAT))
    # sending real message
    client.send(bytes(msg,FORMAT))
    

# for receiving messages from clients
def recv():
    msg_len = client.recv(HEADER).decode(FORMAT)
    if msg_len:
        msg = client.recv(int(msg_len)).decode(FORMAT)
        return msg





download_files_menu()
