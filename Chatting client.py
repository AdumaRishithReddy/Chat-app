import socket
import sys
# import customtkinter
import threading
from datetime import datetime

# customtkinter.set_appearance_mode("dark")
# customtkinter.set_default_color_theme("green")
# root=customtkinter.CTk()
# root.geometry("500x350")
# frame=customtkinter.CTkFrame(master=root)
# frame.pack(pady=29,padx=70,fill="both",expand=True)



now = datetime.now()
dt_str= now.strftime("%d/%m/%Y %H:%M:%S")

c= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port =9989

def listen_resp(c):
    while 1:
        print(end='\n')

        msg=c.recv(1024).decode()
        # print(msg,end='\n')
        if msg != '':
            # username = msg.split("~")[0]
            # content = msg.split('~')[1]
            print(msg + " "+dt_str)
        else :
            print("Empty msg was sent")

def send_msg(c):
    while 1:
        msg=input("Share your thoughts: ")
        print(end='\n')
        if msg !='':
            c.sendall(msg.encode())

        else:
            print("empty msg")
            exit(0)

def com_to_server(c):
    # en1 = cus
    username=input("Please give your username for this session: ")
    if username != '':
        c.sendall(username.encode())
    else:
        print("No username entered")
        exit()
    threading.Thread(target=listen_resp,args=(c,)).start()
    send_msg(c)
    # root.mainloop()

try:
    c.connect(('127.0.0.1',port))
except:
    print("Unable to connect to host")

com_to_server(c)
