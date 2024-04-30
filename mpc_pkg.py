#this is the class to contain all information will be sent to other useres in MPC
#stats is a dictionary with statistics type: value
import sys
from parser_cmd import parser_cmd
from color_output import *
from client import client
import json


class mpc_pkg:
    def __init__(self, host, user_list, stats,share_list):
        self.host=host
        self.user_list=user_list
        self.stats=stats
        self.share_list=share_list
        self.client=client()

    def stats_update(self,new_stats):
        new_type=list(new_stats.keys())[0]
        new_value=list(new_stats.values())[0]
        if new_type in self.stats:
            prYellow("The "+new_type+" type already exists, updating the value from "+str(self.stats[new_type])+" to "+str(new_value))
            self.stats[new_type]=new_value
        else:
            prYellow("Adding new type "+str(new_type)+" with value "+str(new_value))
            self.stats.update(new_stats)


    def states_update_send(self):
        """
        Send the uopdated statistics types to the server
        """
        type_list=[]
        for stats in self.stats:
            type_list.append(stats)
        try:
            ack=self.client.send_to_server(("STAT"+json.dumps(type_list)))
            prCyan(ack)
        except:
            prRed("Error sending statistics to server, please try again.")

    def stats_delete(self,del_stats):
        if del_stats in self.stats:
            del self.stats[del_stats]
            prYellow("Deleted type "+del_stats)
        else:
            prRed("Type "+del_stats+" not found, please try again.")

    def user_update(self,new_user):
        try:
            host=new_user[0]
            port=int(new_user[1])
            self.client.enter_server(host,port)
            self.client.send_to_server("Hello from the client")
            info=json.loads(self.client.send_to_server("INFO"))
            prYellow("Server currently hold a party size of "+str(info[0]))
            for stats in info[1]:
                prYellow("We have "+str(int(info[1][stats]))+ " people want to compute their "+str(stats))
        except:
            prRed("Error connecting to server, please try again.")

    def info_update(self):
        try:
            info=json.loads(self.client.send_to_server("INFO"))
            prYellow("Server currently hold a party size of "+str(info[0]))
            for stats in info[1]:
                prYellow("We have "+str(int(info[1][stats]))+ " people want to compute their "+str(stats))
        except:
            prRed("Error connecting to server, please try again.")
    

    def view_user(self):
        """
        This function is used by old MPC module and will not call in current version
        Keep for future reference
        """
        print("Current party members:")
        for user in self.user_list:
            prPurple(str(user[0])+" : "+str(user[1]))
        prGreen("If you want to delete users, enter DELETE hostname:port\nIf you want to add users, enter ADD hostname:port\nEnter QUIT to finish.")
        curr_input=sys.stdin.readline()
        while curr_input!="QUIT\n":
            change_name=parser_cmd.delete_or_add_user(curr_input)
            if change_name==None:
                prRed("Invalid command, please enter DELETE hostname:port or ADD hostname:port")
            elif change_name[1]==None:
                prRed("Invalid URL entered, please try again with format: hostname:port")
            elif change_name[1].hostname!=None and change_name[1].port!=None and change_name[1].port.isnumeric()==True:
                    if change_name[0]==1:
                        self.delete_user(change_name[1])
                    elif change_name[0]==2:
                        self.user_update([change_name[1].hostname,change_name[1].port])
                        print("Added user",change_name[1].hostname,":",change_name[1].port)
                    print("Change Complete, Current party members:")
                    for user in self.user_list:
                        prPurple(str(user[0])+" : "+str(user[1]))
                    prGreen("Keep editing or enter QUIT to finish.")
            else:
                prRed("Invalid URL entered, please try again with format: hostname:port")
            curr_input=sys.stdin.readline()

    def delete_user(self,del_user):
        """
        This function is used by old MPC module and will not call in current version
        Keep for future reference
        """
        del_user=del_user.hostname+":"+str(del_user.port)
        for user in self.user_list:
            check_user=user[0]+":"+str(user[1])
            if check_user==del_user:
                self.user_list.remove(user)
                print("Deleted user",del_user)
                return
        print("User not found, please try again.")


    def view_stats(self):
        print("Current statistics:")
        for data in self.stats:
            prPurple(str(data)+" : "+str(self.stats[data]))
        prGreen("If you want to delete data, enter DELETE type-of-data\nIf you want to add users, enter ADD type:value\nEnter QUIT to finish.")
        curr_input=sys.stdin.readline()
        while curr_input!="QUIT\n":
            change_name=parser_cmd.delete_or_add_data(curr_input)
            if change_name==None:
                prRed("Invalid command, please enter DELETE type-of-data or ADD type:value")
            elif change_name[1]!=None:
                if change_name[0]==1:
                    self.stats_delete(change_name[1])
                elif change_name[0]==2:
                    self.stats_update(change_name[1])
                print("Change Complete, Current stats data:")
                for data in list(self.stats.items()):
                    prPurple(str(data))
                prGreen("Keep editing or enter QUIT to finish.")
            else:
                prRed("Invalid data pair entered, please try again with format: type:value")
            curr_input=sys.stdin.readline()
        self.states_update_send()

# Currently, these computations will not calculate the statistics across data from multiple users in MPC.
# They use the stats from the locally stored stats dictionary of the instance.
# Goal is to be able to aggregate the local computations across all instances which will be further implemented later.

    def compute_sum(self):
        summed_stats = {}
        prGreen("Calculating sum of statistics. Please input the statistics data type you want to compute(eg.age):")
        stat_type = sys.stdin.readline().strip()
        self.client.send_to_server("CALC SUM "+stat_type)
        for stat_type, values in self.stats.items():
            if isinstance(values, list) and all(isinstance(x, (int, float)) for x in values):
                summed_stats[stat_type] = sum(values)
            else:
                prRed("Error calculating sum.")
        print("Sum: ", summed_stats)
        return summed_stats
    
    '''
        def compute_average(self):
        summed_stats = self.compute_sum()
        average_stats = {}
        for stat_type, sum_value in summed_stats.items():
            if stat_type in self.stats and isinstance(self.stats[stat_type], list) and len(self.stats[stat_type]) > 0:
                 average_stats[stat_type] = sum_value / len(self.stats[stat_type])
            else:
                prRed("Error computing average.")
        print("Average: ", average_stats)
        return average_stats
    
    def compute_max(self):
        max_stats = {}
        for stat_type, values in self.stats.items():
            if isinstance(values, list) and values:
                max_stats[stat_type] = max(values)
            else:
                prRed("Error calculating max value.")
        print("Max: ", max_stats)
        return max_stats
    
    def compute_min(self):
        min_stats = {}
        for stat_type, values in self.stats.items():
            if isinstance(values, list) and values:
                min_stats[stat_type] = min(values)
            else:
                prRed("Error calculating minimum value.")
        print("Minimum: ", min_stats)
        return min_stats'''
    
    #def party_init(self):
        