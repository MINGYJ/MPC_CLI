"""
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
        """
        Retrieve personal data from 'share_to_send' and retrieve party data from 'share_received'
        """
        party_data = []
        # Merge personal shares and received shares logic here
        for personal_share_file, received_share_file in zip(os.listdir(self.personal_shares), os.listdir(self.received_shares)):
            personal_share_path = os.path.join(self.personal_shares, personal_share_file)
            received_share_path = os.path.join(self.received_shares, received_share_file)
            if os.path.isfile(personal_share_path) and os.path.isfile(received_share_path):
                with open(personal_share_path, 'r') as personal_file, open(received_share_path, 'r') as received_file:
                    personal_share = int(personal_file.read().strip())
                    received_share = int(received_file.read().strip())
                    
                    # Merge shares
                    merged_share = personal_share + received_share
                    party_data.append(merged_share)
        return party_data

    def read_data(self, directory):
        """
        Iterate over files to retrieve the numerical data
        """
        merged_data = []
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath):
                with open(filepath, 'r') as file:
                    # Read numerical data from file and append to merged_data
                    data = file.read().strip()
                    # Assuming data is a single numerical value per file
                    if data.isdigit():
                        merged_data.append(int(data))
        return merged_data    
    