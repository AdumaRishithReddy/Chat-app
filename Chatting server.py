import socket
# import customtkinter
import threading
from datetime import datetime
now = datetime.now()
dt_str= now.strftime("%d/%m/%Y %H:%M:%S")
all_clients=[]
def listen_resp(c,username):
    while 1:
        msg=c.recv(1024).decode()
        if msg != '':
            final_msg= username+'~'+ msg
            send_to_all(final_msg)
        else:
            print("No msg sent")

def send_to_all(message):
    for user in all_clients:
        user[1].sendall(message.encode())
def client_handler(c):
    while 1:
        username =c.recv(1024).decode()
        if username != '':
            all_clients.append((username,c))
            break
        else:
            print("Username is not given")
    threading.Thread(target=listen_resp,args=(c,username,)).start()



s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created")

port = 9989

s.bind(('127.0.0.1',port))
print("socket bound to %s" %(port))

s.listen(4)
print("Socket is listening")
# s.connect(('127.0.0.1',1235))
while (True):
    c,addr=s.accept()
    print('Got connected to ',addr)
    threading.Thread(target=client_handler, args=(c,)).start()
    # data1 = c.recv(1024)
    # print(data1.decode());
    c.send('Thanks for using my server'.encode())


