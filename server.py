## this is used to create a party list and make sure each memeber know others
##get part of code ideas (broadcast) from https://github.com/IamLucif3r/Chat-On with MIT License

import threading
import socket
import json
from color_output import *
import pickle

try:
    # Now this Host is the IP address of the Server, over which it is running.
    # I've user my localhost.
    host = socket.gethostbyname(socket.gethostname())
    port = 7777  # Choose any random port which is not so common (like 80)

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




# 1.MPC Calculation Broadcasting Method
def calc_broadcast(command,stats,clients_list):
    print(command,stats,clients_list)
    for client in clients_list:
        send_clients=clients_list
        send_clients.remove(client)
        send_clients=[x.getpeername() for x in send_clients]
        message="CALC "+command+" "+stats+" "+json.dumps(send_clients)
        client.send(message.encode('ascii'))

# 2.Broadcasting Method
def broadcast(message):
    print('Broadcasting:',message.decode('ascii'))
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
            elif message[0:4]=='CALC':
                message=message.split()
                if message[1]=='SUM':
                    stats=message[2]
                    client.send("ACK COMPUTATION".encode('ascii'))
                    if stats in stats_types:
                        broadcast_clients=get_type_client_list(stats)
                        calc_broadcast("SUM",stats,broadcast_clients)
                elif message[1]=='AVG':
                    stats=message[2]

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

#return the clients have *type needed in their data
def get_type_client_list(type):
    client_list=[]
    for i,stats in enumerate(clients_stats):
        if type in stats:
            client_list.append(clients[i])
    return client_list


# Calling the main method
prRed('This is the trusted third party server, please make sure it does not engaged in computation.')
prGreen('Party Server is Listening over the IP: '+str(host)+' and Port: '+str(port))
receive()
while True:
    if clients!=None:
        broadcast("CALC SUM age {1,2,3,4,5}".encode('ascii'))
        print('Broadcasted')





