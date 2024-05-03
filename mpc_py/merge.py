"""
This module contains functions that are in charge of:
1. Retrieving the relevant computed results of all parties.
2. Merging the computed results to produce a statistical output that includes the values of all parties.

Thought/Question for Group Meeting: 

For each party member are we retrieving files from both 'share_to_send' and 'share_received'? 
For example, using the party member's personal data from 'share_to_send' in combination with the shares they received from other party members in 'share_received" to calculate the entire parties result?
How to gather these data inputs, store them, and run them through server_func.py for calculations?
"""
import os

class merge:
    def __init__(self, personal_shares, received_shares):
        self.personal_shares = personal_shares
        self.received_shares = received_shares
        

    def merge_data(self):
        party_data = []
        #retrieve personal data from 'share_to_send'
        #retrieve party data from 'share_received'
        return party_data
    
    def read_data(self, directory):
        merged_data = []
        #Iterate over the files and retrieve the numerical data.
        return merged_data
    
    


    