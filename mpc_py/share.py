""" 
This module contains functions that are in charge of:
1. Retrieving the input and it's data type.
2. Outputting the share file into the share_to_send folder.
3. Naming the file ("share_format.txt).
"""

import os
import shamirs
import pickle

class share:
    share_data=0
    share_type=''
    party_size=1

def shares(input, type, num_shares, output):
    """
    Generate shares for input data using Shamir's Secret Sharing algorithm
    and save them to a file.

    Parameters:
        input: The input data to be shared.
        type: Type of input data.
        num_shares: Number of shares to be generated
        output: Folder path to save the share file.
    """

    shares = SecretSharer.split_secret(str(input), num_shares)

    share_inst = share()
    share_inst.share_data = input
    share_inst.share_type = type
    share_inst.party_size = num_shares

    file_name = f"share_{type}.txt"
    file_path = os.path.join(output, file_name)

    with open(file_path, 'w') as f:
        f.write(f"Share Type: {type}\n")
        for share_index, share_value in shares:
            f.write(f"Share Index: {share_index}, Share Value: {share_value}\n")

    print(f"Shares saved to {file_path}")
