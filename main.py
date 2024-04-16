from socket import *
import sys
from parser_cmd import parser_cmd
from mpc_pkg import mpc_pkg
#from colorama import Fore, Back, Style

party_size=1


hostname=gethostname()
print("Hello! Hostname: ",hostname)
print("IP Address: ",gethostbyname(hostname))
print("Please start entering the other users hostname:port to start. Enter QUIT to finish entering users.")
Curr_user=mpc_pkg(hostname,[],[])
url_input=sys.stdin.readline()


#this part is use for collecting information of other users in the party
#maybe implement a file import method in the future
while url_input!="QUIT\n":
    parsed_url=parser_cmd.host_port(url_input)
    if parsed_url==None:
        print("Invalid URL entered, please try again with format: hostname:port")
    else:
        print("You entered hostname: ",parsed_url.scheme, " and port: ",parsed_url.path)
        #use hostname:port so the real netloc become scheme, the port is in "path" section
        party_size+=1
        print("Now enter information for the next user. \nEnter QUIT to finish entering users. Current party size: ",party_size)
    url_input=sys.stdin.readline()
print("Finish entering users.\nWe have",party_size,"users in the party.")

#start entering statistics the user want to share in MPC
