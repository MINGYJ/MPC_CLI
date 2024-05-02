"""
This module contains functions that are in charge of:
1. Integrating the three MPC programs: merge, serve_func, and share.
2. Handling and bridging files from three different folders.
3. Initiliazing computations needed for our statistical results. 

Streamline:
1. Function calls 'share' to retrieve the share of a value.
2. Call a function from 'server_func' to compute the specified statistic.
3. Call the function from 'merge' to merge the results of all three servers.

Note: The methods in the three MPC programs only need to deal with numbers, not files.

"""

def compute_sum(command,party_size,stats):
    #parameter eg. command='age',party_size=3,stats=20
    #need to output two shares in files and save in share_to_send and one share in share_received
    #can use json dump for save in files
    #file name would be SUM_age_3.txt
    #file format could be same as what we create in Lab2, but be able to handle party size larger than 2
    