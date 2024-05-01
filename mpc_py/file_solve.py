"""
This module contains the function as a bridge between files from three folder and the other three MPC programs: merge , server_func and share
This function will call the function from share to get the share of a value
After communication complete, it will call the function from server_func to compute the value
Finally, it will call the function from merge to merge the result from all three servers
the method in merge, server_func and share only need to deal with *number*, not files

"""

def compute_sum(command,party_size,stats):
    #parameter eg. command='age',party_size=3,stats=20
    #need to output two shares in files and save in share_to_send and one share in share_received
    #can use json dump for save in files
    #file name would be SUM_age_3.txt
    #file format could be same as what we create in Lab2, but be able to handle party size larger than 2
    