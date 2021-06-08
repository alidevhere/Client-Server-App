import socket

HEADER = 64
PORT = 12345
FORMAT = 'utf-8'
SERVER = '127.0.0.1'
ADDR = (SERVER,PORT)
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)
print(f'[CONNECTED] : connected to " {SERVER} ".')

def receive_file(client,file_name):
    file_len = client.recv(HEADER).decode(FORMAT)
    if file_len:
        file_data = client.recv(int(file_len)).decode(FORMAT)
        f = open(f'client\{file_name}','w')
        f.write(file_data)
        f.close()
    



def download_files_menu():
    # files names string header
    msg_len = client.recv(HEADER).decode(FORMAT)
    if msg_len:
        print('FILE DOWNLOAD MENU\n')
        msg = client.recv(int(msg_len)).decode(FORMAT)
        file_name = input(f'Choose a file to download:\n{msg}')
        file_name_len = str(len(file_name))
        file_name_len += ' ' * (HEADER-len(file_name))
        client.send(bytes(file_name_len,FORMAT))
        client.send(bytes(file_name,FORMAT))
        receive_file(client,file_name)
    else:
        print('[ERROR]: No files found on server.')
        

download_files_menu()
