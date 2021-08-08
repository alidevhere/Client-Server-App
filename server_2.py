import socket as s
import os
import threading
import tqdm

PORT = 12345
SERVER_IP_ADDRESS='0.0.0.0'
BUFFER_SIZE =4096



def start_server():
    client = s.socket()
    print('Waiting for connections...')
    client.bind((SERVER_IP_ADDRESS,PORT))
    client.listen(5)
    while True:
        print('[STATUS]: Waiting for connections.')
        con,addr=client.accept()
        try:
            t=threading.Thread(target=handle_connection,args=(con,addr))
            t.start()
            print(f'[ + ]: {addr} connected.')
            print(f'[ COUNT ] : thread count = {threading.active_count()}')
        except:
            print(f'[ EXCEPTION ] : ERROR in connection to "{addr}" ')
        


def handle_connection(con,addr):
    send_file_menu(con,addr)
    file_name = con.recv(BUFFER_SIZE).decode()
    print(f'[ DOWNLOAD ] : file "{file_name}" requested  by "{addr}" for downloading')
    file_size=os.path.getsize(f'server/{file_name}')
    progress = tqdm.tqdm(range(file_size), f"Sending {file_name}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(f'server/{file_name}','rb') as f:
        while True:
            data = f.read(BUFFER_SIZE)
            if not data :
                break
            con.sendall(data)
            progress.update(len(data))
            print('')

    con.close()
            #print(f'{len(data)} sent...')    
    
    #con.send('Welcome to connection.'.encode())
    






def files_str(files):
    s =''
    for f in files:
        s+=f+'\n'    
    return s


def send_file_menu(con,addr):

    files = os.listdir(os.path.join(os.getcwd(),'server'))
    msg = files_str(files)
    con.send(msg.encode())

start_server()
