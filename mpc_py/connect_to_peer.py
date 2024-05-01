"""
This class is used for connect to peers and listen to peers.
If there is 3 people in the party, the server will open 4 threads, 2 for listen to other two, and 2 for sending to other 2
This class will use the file generate by file_solve.py
"""
import socket
import threading
from ..color_output import *
import os
import glob

class connect_to_peer:

    def __init__(self,command,client) -> None:
        self.command=command
        client=client.getsockname()
        self.host = client[0]
        self.port = client[1]+1
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen()
        print("Peer Server is listening on",self.host,":",self.port)
        self.client_list=[]
        self.receive()

    def receive(self):
        while True:
            client, address = self.server.accept()
            print(f"Connected with {str(address)}")
            print('Connected to the',client)
            # Ask the clients for Nicknames
            client.send(('HELLO FROM '+str(self.host)).encode('ascii'))
            #add client to list
            self.client_list.append(client)
            # Handling Multiple Clients Simultaneously
            thread = threading.Thread(target=self.handle, args=(client,))
            thread.start()

    def handle(self,client):
        while True:
            try:
                calc=self.command[1]
                stats=self.command[2]
                file_name=str(calc)+"_"+str(stats)+"_"+len(self.client_list)+".txt"
                f = open('../share_received/'+file_name,'w+')
                l = client.recv(1024)
                while (l):
                    f.write(l)
                    l = client.recv(1024)
                f.close()
                prCyan ("Done Receiving")
            except  Exception as e:
                print("Error in handle",e)
                break

    def send(self):
        #send the file in share_to_send to every other people in the party
        peer_lists=self.command[3]
        for peer in peer_lists:
            send_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            send_client.connect((peer[0], peer[1]))
            file_name="./share_to_send/"+str(self.command[1])+"_"+str(self.command[2])+"*.txt"
            #since the peer receiving side is handle by multi-thread, sending can be a single thread to reduce resource usage
            f=open(glob.glob(file_name)[0])
            print("**Current Sending files",glob.glob(file_name))
            

