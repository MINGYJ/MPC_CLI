#the function takes input, input data type
#output the share file into the share_to_send folder
#the name of the file is the share_format.txt

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

    # Save shares to file
    file_name = os.path.join(output, 'share_format.txt')

    with open(file_name, 'w') as f:
        f.write(f"Share Type: {type}\n")
        for share_index, share_value in shares:
            f.write(f"Share Index: {share_index}, Share Value: {share_value}\n")

    print(f"Shares saved to {file_name}")
