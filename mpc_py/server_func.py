#this is the class to compute Shamir's secret shares
#currently finish add/mult

import os

class server_func:

    path='../share_received/'

    def __init__(self):
        pass

    def add(self,range):
        share_add=0
        inDir = os.listdir(self.path)
        for share_recv in inDir:
            entire_path = os.path.join(self.path, share_recv)
            with open(entire_path, 'r') as file:
                for line in file:
                    share_add += int(line.strip())
        return share_add
    
    def average(self, range):
        share_sum=0
        count=0
        inDir = os.listdir(self.path)
        for share_recv in inDir:
            entire_path = os.path.join(self.path, share_recv)
            with open(entire_path, 'r') as file:
                for line in file:
                    share_sum += float(line.strip())
                    count+=1
        return share_sum/count
        
    def max(self, range):
        max_value = None
        inDir = os.listdir(self.path)
        for share_recv in inDir:
            entire_path = os.path.join(self.path, share_recv)
            with open(entire_path, 'r') as file:
                for line in file:
                    max_share = float(line.strip())
                    if max_share > max_value or max_value is None:
                        max_value = max_share
        return max_value

    def min(self, range):
        min_value = None
        inDir = os.listdir(self.path)
        for share_recv in inDir:
            entire_path = os.path.join(self.path, share_recv)
            with open(entire_path, 'r') as file:
                for line in file:
                    min_share = float(line.strip())
                    if min_share < min_value or min_value is None:
                        min_value = min_share
        return min_value