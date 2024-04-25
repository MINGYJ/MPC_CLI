## this is used to create a party list and make sure each memeber know others
##get part of code ideas (broadcast) from https://github.com/IamLucif3r/Chat-On with MIT License

import threading
import socket
import json
from color_output import *

try:
    # Now this Host is the IP address of the Server, over which it is running.
    # I've user my localhost.
    host = socket.gethostbyname(socket.gethostname())
    port = 5555  # Choose any random port which is not so common (like 80)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the server to IP Address
    server.bind((host, port))
    # Start Listening Mode
    server.listen()
    # List to contain the Clients getting connected
    clients = []
    #2d array to store the clients and their static 
    clients_stats=[]
    #set to store all statistic types (age, salary etc)
    stats_types=[]
except socket.error as e:
    print(str(e))




# 1.Broadcasting Method
def broadcast(message):
    print(message.decode('ascii'))
    for client in clients:
        client.send(message)



def handle(client):
    while True:
        try:
            msg = message = client.recv(1024)
            message=message.rstrip(b'\0')
            print('Message:',message)
            message = message.decode('ascii')
            if message[0:4] == 'STAT':
                #get the client statics type (e.g. age)
                types=json.loads(message[4:])
                print('KNOW INFO:',types)
                clients_stats[clients.index(client)]=types
                for stats in types:
                    if stats not in stats_types:
                        stats_types.append(stats)
                client.send("ACK by Server".encode('ascii'))
            elif message[0:4]=='INFO':
                info=[len(clients),get_info()]
                info=json.dumps(info)
                client.send(info.encode('ascii'))
            else:
                client.send("ACK".encode('ascii'))
        except socket.error:
            if client in clients:
                index = clients.index(client)
                # Index is used to remove client from list after getting disconnected
                clients.remove(client)
                clients_stats.pop(index)
                client.close()
                broadcast(f'{client} left the Party!'.encode('ascii'))
                break


# Main Receive method
def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")
        print('Connected to the',client)
        # Ask the clients for Nicknames
        client.send(('HELLO FROM '+str(host)).encode('ascii'))
        #add client to list
        clients.append(client)
        clients_stats.append([])
        # Handling Multiple Clients Simultaneously
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

def get_info():
    info={}
    for stats in stats_types:
        count=sum(x.count(stats) for x in clients_stats)
        if count>0:
            info[stats]=count
    return info


# Calling the main method
prRed('This is the trusted third party server, please make sure it does not engaged in computation.')
prGreen('Party Server is Listening over the IP: '+str(host)+' and Port: '+str(port))
receive()





