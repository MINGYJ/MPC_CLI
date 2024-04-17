from socket import *
import sys
from parser_cmd import parser_cmd
from mpc_pkg import mpc_pkg
from color_output import *
#from colorama import Fore, Back, Style

party_size=1

try:
    hostname=gethostname()
    print("Hello! Hostname: ",hostname)
    print("IP Address: ",gethostbyname(hostname))
except:
    prRed("Unable to get Hostname and IP, try restarting the program.")

prGreen("Please start entering the other users hostname:port to start. Enter QUIT to finish entering users.")
Curr_user=mpc_pkg(hostname,[],{},[])
url_input=sys.stdin.readline()


#this part is use for collecting information of other users in the party
#maybe implement a file import method in the future
while url_input!="QUIT\n":
    parsed_url=parser_cmd.host_port(url_input)
    if parsed_url==None or parsed_url.hostname==None or parsed_url.port.isnumeric()==False:
        prRed("Invalid URL entered, please try again with format: hostname:port")
    else:
        prYellow("You entered hostname:"+parsed_url.hostname+" and port:"+parsed_url.port)
        #use hostname:port so the real netloc become hostname, the port is in "port" section
        party_size+=1
        Curr_user.user_update([parsed_url.hostname,parsed_url.port])
        prGreen("Now enter information for the next user. \nEnter QUIT to finish entering users. Current party size: "+str(party_size))
    url_input=sys.stdin.readline()
print("Finish entering users.\nWe have",party_size,"users in the party.")


#start entering statistics the user want to share in MPC
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nNow Entering the statistic data you want to share in MPC")
prGreen("Please enter the statistic type and value in the format: type:value\nEnter QUIT to finish entering statistics.")
curr_stat=sys.stdin.readline()
while curr_stat!="QUIT\n":
    parsed_stat=parser_cmd.stats_type(curr_stat)
    if parsed_stat==None:
        prRed("Invalid format, please enter in the format: type:value")
    else:
        Curr_user.stats_update(parsed_stat)
        #print("You entered data with type",list(parsed_stat.keys())[0],"and value",list(parsed_stat.values())[0])
        prGreen("Now enter the next statistic data. \nEnter QUIT to finish entering statistics.")
    curr_stat=sys.stdin.readline()
print("Finish entering statistics.\nWe have",len(Curr_user.stats),"statistics to share in MPC.")

#now we can start calculating
#will implement the TCP communication part in the next update
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
prGreen("All data prepared, \nenter USER to view and edit all party members hostname, \nenter DATA to view and edit the statistics data you just input, \nenter CALC to start computing stage.")
curr_input=sys.stdin.readline()
while curr_input!="CALC\n":
    if curr_input=="USER\n":
        Curr_user.view_user()
    elif curr_input=="DATA\n":
        Curr_user.view_stats()
    prGreen("Enter USER to view and edit all party members hostname, \nEnter DATA to view and edit the statistics data you just input, \nEnter CALC to start computing stage.")
    curr_input=sys.stdin.readline()