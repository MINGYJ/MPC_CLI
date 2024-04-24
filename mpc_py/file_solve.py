"""
This module contains the function as a bridge between files from three folder and the other three MPC programs: merge , server_func and share
This function will call the function from share to get the share of a value
After communication complete, it will call the function from server_func to compute the value
Finally, it will call the function from merge to merge the result from all three servers
the method in merge, server_func and share only need to deal with *number*, not files

"""