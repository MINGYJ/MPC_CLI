import socket
import threading
import json
import os
from color_output import *


class client:

    def __init__(self):
        self.client = None
        self.stop_thread = False
        self.receive_message = None
        self.mpc_cmd=None
        # self.client_start()

    def enter_server(self,ip,port):
        # Store the ip and port number for connection
        try:
            # ip = input("Enter the ip address of the server:")
            # port = int(input("Enter the port number of the server:"))
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Connect to a host
            self.client.connect((ip, port))
            prCyan(self.client.recv(1024).decode('ascii'))
            self.receive_thread = threading.Thread(target=self.receive)
            self.receive_thread.start()
        except:
            print('Error Occured while Connecting, maybe info is wrong, try again')
            self.enter_server()


    def receive(self):
        while True:
            if self.stop_thread:
                break
            else:
                try:
                    message = self.client.recv(1024).decode('ascii')
                    # Clients those are banned can't reconnect
                    #prCyan("thread recv:"+message)
                    if self.calc_event(message):
                        self.receive_message=None
                    else:
                        self.receive_message = message
                except socket.error:
                    print('Error Occured while Connecting, maybe server is down')
                    self.client.close()
                    break
        

    def calc_event(self,message):
        if message[0:4]=="CALC":
            prCyan("++++++++++++++\nReceived Calculcation Command\n++++++++++++++")
            self.mpc_cmd=message
            self.receive_message=None
            return True
                    

    def send_to_server(self,message):
        try:
            self.clear_buffer()
            msg=message.encode('ascii')
            msg=msg.ljust(1024,b'\0')
            #padding to make all msg have same length-same socket size
            self.client.send(msg)
            while self.receive_message == None: continue
            recv=self.receive_message
            self.receive_message = None
            #print('Received:',recv)
            return recv
        except socket.error as e:
            print('Error Occured while Connecting, maybe server is down')
            self.client.close()



    def client_start(self):
        try:
            global stop_thread
            # self.enter_server()
            stop_thread = False
            receive_thread = threading.Thread(target=self.receive)
            receive_thread.start()
            self.send_to_server("Hello from the client")
        except socket.error as e:
            return False
        
    def clear_buffer(self):
        sock=self.client
        sock.setblocking(0)
        while True:
            try:
                sock.recv(1024)
            except BlockingIOError:
                sock.setblocking(1)
                return
    
    def get_socket(self):
        return self.client

# client=client()
# print("Client Started")
# client.enter_server("10.106.208.86",5555)
# client.send_to_server("STAT"+json.dumps(["age","salary","height","weight"]))