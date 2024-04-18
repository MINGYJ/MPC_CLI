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
            return