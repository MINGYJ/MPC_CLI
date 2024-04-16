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
Curr_user=mpc_pkg(hostname,[],{},[])
url_input=sys.stdin.readline()


#this part is use for collecting information of other users in the party
#maybe implement a file import method in the future
while url_input!="QUIT\n":
    parsed_url=parser_cmd.host_port(url_input)
    if parsed_url==None or parsed_url.path.isnumeric()==False:
        print("Invalid URL entered, please try again with format: hostname:port")
    else:
        print("You entered hostname:",parsed_url.scheme, " and port:",parsed_url.path)
        #use hostname:port so the real netloc become scheme, the port is in "path" section
        party_size+=1
        Curr_user.user_update([parsed_url.scheme,parsed_url.path])
        print("Now enter information for the next user. \nEnter QUIT to finish entering users. Current party size: ",party_size)
    url_input=sys.stdin.readline()
print("Finish entering users.\nWe have",party_size,"users in the party.")


#start entering statistics the user want to share in MPC
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nNow Entering the statistic data you want to share in MPC")
print("Please enter the statistic type and value in the format: type:value\nEnter QUIT to finish entering statistics.")
curr_stat=sys.stdin.readline()
while curr_stat!="QUIT\n":
    parsed_stat=parser_cmd.stats_type(curr_stat)
    if parsed_stat==None:
        print("Invalid format, please enter in the format: type:value")
    else:
        Curr_user.stats_update(parsed_stat)
        #print("You entered data with type",list(parsed_stat.keys())[0],"and value",list(parsed_stat.values())[0])
        print("Now enter the next statistic data. \nEnter QUIT to finish entering statistics.")
    curr_stat=sys.stdin.readline()
print("Finish entering statistics.\nWe have",len(Curr_user.stats),"statistics to share in MPC.")

#now we can start calculating
#will implement the TCP communication part in the next update
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nAll data prepared, enter USER to print all party members hostname, enter DATA to view the statistics data you just input, enter CALC to enter computing stage.")
curr_input=sys.stdin.readline()
while curr_input!="QUIT\n":
