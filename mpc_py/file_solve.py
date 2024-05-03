import os
from .server_func import server_func
from .merge import merge

def compute_sum(command,party_size,stats):
    #parameter eg. command='age',party_size=3,stats=20
    #need to output two shares in files and save in share_to_send and one share in share_received
    #can use json dump for save in files
    #file name would be SUM_age_3.txt
    #file format could be same as what we create in Lab2, but be able to handle party size larger than 2
    pass

def compute_average(command, party_size, stats):
    pass

def compute_max(command, party_size, stats):
    pass

def compute_min(command, party_size, stats):
    pass

"""
Currently, to compute ALL the functions, however I believe our goal is to let the user calculate the statistic of their choosing.

def party_computation(self, party_data):
        #Run the numerical data through server_func to calculate.
        return {
            'sum': server_func.add(party_data),
            'average': server_func.average(party_data),
            'max': server_func.max(party_data),
            'min': server_func.min(party_data)
        }
    
def final_result(self):
        final_output = self.all_data()
        results = self.computation(final_output)
        print("Party Computation Results: ", results)

        """