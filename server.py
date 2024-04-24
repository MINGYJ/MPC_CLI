## this is used to create a party list and make sure each memeber know others
##get this structure from https://github.com/IamLucif3r/Chat-On with MIT License

import threading
import socket

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
except socket.error as e:
    print(str(e))




# 1.Broadcasting Method
def broadcast(message):
    for client in clients:
        client.send(message)



def handle(client):
    while True:
        try:
            msg = message = client.recv(1024)
            broadcast(message)  # As soon as message received, broadcast it.

        except socket.error:
            if client in clients:
                index = clients.index(client)
                # Index is used to remove client from list after getting disconnected
                client.remove(client)
                client.close()
                broadcast(f'{client} left the Chat!'.encode('ascii'))
                break


# Main Receive method
def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")
        # Ask the clients for Nicknames
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        # If the Client is an Admin prompt for the password.
        with open('bans.txt', 'r') as f:
            bans = f.readlines()

        if nickname + '\n' in bans:
            client.send('BAN'.encode('ascii'))
            client.close()
            continue

        if nickname == 'admin':
            client.send('PASS'.encode('ascii'))
            password = client.recv(1024).decode('ascii')
            # I know it is lame, but my focus is mainly for Chat system and not a Login System
            if password != 'adminpass':
                client.send('REFUSE'.encode('ascii'))
                client.close()
                continue

        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname of the client is {nickname}')
        broadcast(f'{nickname} joined the Chat'.encode('ascii'))
        client.send('Connected to the Server!'.encode('ascii'))

        # Handling Multiple Clients Simultaneously
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()




# Calling the main method
print('Server is Listening over the IP:', host,' and Port:', port)
receive()

# MIT License

# Copyright (c) 2021 Anmol Singh Yadav

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.