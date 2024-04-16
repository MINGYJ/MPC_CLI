#this is the class to contain all information will be sent to other useres in MPC
#stats is a dictionary with statistics type: value
import sys
from parse import *

class mpc_pkg:
    def __init__(self, host, user_list, stats,share_list):
        self.host=host
        self.user_list=user_list
        self.stats=stats
        self.share_list=share_list

    def stats_update(self,new_stats):
        new_type=list(new_stats.keys())[0]
        new_value=list(new_stats.values())[0]
        if new_type in self.stats:
            print("The",new_type,"type already exists, updating the value from",self.stats[new_type],"to",new_value)
            self.stats[new_type]=new_value
        else:
            print("Adding new type",new_type,"with value",new_value)
            self.stats.update(new_stats)

    def user_update(self,new_user):
        new_user=[new_user[0],int(new_user[1])]
        self.user_list.append(new_user)

    def view_user(self):
        print("Current party members:")
        for user in self.user_list:
            print(user[0],":",user[1])
        print("If you want to delete, enter DELETE hostname:port\n If you want to add, enter ADD hostname:port")
        curr_input=sys.stdin.readline()
        if curr_input[0:4]=="DELETE":
            delete_user=curr_input.split(" ")[1]
            for user in self.user_list:
                check_user=user[0]+":"+str(user[1])
                if check_user==delete_user:
                    self.user_list.remove(user)
                    print("Deleted user",delete_user)
                    break
        elif curr_input[0:3]=="ADD":
            add_user=curr_input.split(" ")[1]
            parsed_url=parser_cmd.host_port(add_user)
            if parsed_url==None or parsed_url.path.isnumeric()==False:
                print("Invalid URL entered, please try again with format: hostname:port")
            else:
                print("You entered hostname:",parsed_url.scheme, " and port:",parsed_url.path)
                #use hostname:port so the real netloc become scheme, the port is in "path" section
                self.user_update([parsed_url.scheme,parsed_url.path])
                print("Now enter information for the next user. \nEnter QUIT to finish entering users. Current party size: ",party_size)
