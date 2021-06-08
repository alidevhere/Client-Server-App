import socket

HEADER = 64
PORT = 12345
FORMAT = 'utf-8'
SERVER = '127.0.0.1'
ADDR = (SERVER,PORT)
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)



def receive_file(client,file_name):
    file_len = client.recv(HEADER).decode(FORMAT)
    if file_len:
        file_data = client.recv(int(file_len)).decode(FORMAT)
        f = open(f'client\{file_name}','w')
        f.write(file_data)
        f.close()
    



def connect():
    client.connect(ADDR)
    msg_len = client.recv(HEADER).decode(FORMAT)
    if msg_len:
        msg = client.recv(int(msg_len)).decode(FORMAT)
        file_name = input(f'Choose a file to download:\n{msg}')
        file_name_len = str(len(file_name))
        file_name_len += ' ' * (HEADER-len(file_name))
        client.send(bytes(file_name_len,FORMAT))
        client.send(bytes(file_name,FORMAT))
        receive_file(client,file_name)

        

connect()

'''
#
file = s.recv(1024)
while file:
    print(file)
    files = s.recv(1024)

# receiving file data
f = open('client\data.txt','wb')
data = s.recv(1024)
while data:
    f.write(data)
    print(data)
    data = s.recv(1024)
f.close()

#s.sendall(b'DONE')

s.shutdown(0)
print('written successfully')
print('connection closed')    
s.close()
'''