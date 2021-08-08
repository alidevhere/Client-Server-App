import socket as s

BUFFER_SIZE=4096
SERVER_IP_ADDRESS='192.168.0.102'
PORT=12345

def start_client():
    client=s.socket()
    client.connect((SERVER_IP_ADDRESS,PORT))
    msg = client.recv(BUFFER_SIZE).decode()
    print(msg)
    file_name=input('\nChoose file to download: ')
    client.send(file_name.encode())

    print('[ DOWNLOADING ]: file downloading......')

    with open(f'client/{file_name}','wb') as f:
        while True:
            data = client.recv(BUFFER_SIZE)
            if not data:
                break
            f.write(data)
    close_connection = True if input('Close Connection ? [Y/N]')== 'Y'  else False

start_client()