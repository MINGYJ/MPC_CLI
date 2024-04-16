#this is the class to contain all information will be sent to other useres in MPC
#stats is a dictionary with statistics type: value

class mpc_pkg:
    def __init__(self, host, user_list, stats,share_list):
        self.host=host
        self.user_list=user_list
        self.stats=stats
        self.share_list=share_list

    def stats_update(self,new_stats):
        new_stats=new_stats.lower()
        
