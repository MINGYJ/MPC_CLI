import json
import os
import shutil

from .share import shares
from .server_func import server_func
from .merge import merge

server = server_func()
merger = merge()

# Parameter eg. command='age',party_size=3,stats=20
def compute_sum(command,party_size,stats):
    """
    Compute the sum of statistics for a given command and party size.
    """

    # Run the numerical data through server_func to calculate the sum
    sum_result = server_func.sum(stats)

    # Split the sum result into shares
    shares_instance = shares(sum_result, 'sum', party_size, 'share_to_send')

    # Merge the shares
    merged_shares = merge.merge(shares_instance)

    # Save the merged shares into a file
    merge_file_name = f"SUM_{command}_{party_size}.txt"
    merge_file_path = os.path.join('share_to_send', merge_file_name)
    with open(merge_file_path, 'w') as merge_file:
        json.dump(merged_shares.__dict__, merge_file)
    
    return sum_result

def compute_average(command, party_size, stats):
    """
    Compute the average of statistics for a given command and party size.
    """

    # Run the numerical data through server_func to calculate the average
    average_result = server_func.average(stats)

    # Split the average result into shares
    shares_instance = shares(average_result, 'average', party_size, 'share_to_send')

    # Merge the shares
    merged_shares = merge.merge(shares_instance)

    # Save the merged shares into a file
    merge_file_name = f"AVERAGE_{command}_{party_size}.txt"
    merge_file_path = os.path.join('share_to_send', merge_file_name)
    with open(merge_file_path, 'w') as merge_file:
        json.dump(merged_shares.__dict__, merge_file)

    return average_result

def compute_max(command, party_size, stats):
    """
    Compute the maximum of statistics for a given command and party size.
    """
    
    # Run the numerical data through server_func to calculate the maximum
    max_result = server_func.max(stats)

    # Split the max result into shares
    shares_instance = shares(max_result, 'max', party_size, 'share_to_send')

    # Merge the shares
    merged_shares = merge.merge(shares_instance)

    # Save the merged shares into a file
    merge_file_name = f"MAX_{command}_{party_size}.txt"
    merge_file_path = os.path.join('share_to_send', merge_file_name)
    with open(merge_file_path, 'w') as merge_file:
        json.dump(merged_shares.__dict__, merge_file)

    return max_result


def compute_min(command, party_size, stats):
    """
    Compute the minimum of statistics for a given command and party size.
    """
    
    # Run the numerical data through server_func to calculate the minimum
    min_result = server_func.min(stats)

    # Split the min result into shares
    shares_instance = shares(min_result, 'min', party_size, 'share_to_send')

    # Merge the shares
    merged_shares = merge.merge(shares_instance)

    # Save the merged shares into a file
    merge_file_name = f"MIN_{command}_{party_size}.txt"
    merge_file_path = os.path.join('share_to_send', merge_file_name)
    with open(merge_file_path, 'w') as merge_file:
        json.dump(merged_shares.__dict__, merge_file)

    return min_result

def send_share_files():
    """
    Send share files from 'share_to_send' folder.
    """
    
    share_to_send_dir = 'share_to_send'
    share_received_dir = 'share_received'

    # Ensure the share_received folder exists
    if not os.path.exists(share_received_dir):
        os.makedirs(share_received_dir)

    # Get list of files in the share_to_send folder
    files_to_send = os.listdir(share_to_send_dir)

    for file_name in files_to_send:
        file_path = os.path.join(share_to_send_dir, file_name)
        if os.path.isfile(file_path):
            # Send the file (implementation depends on the specific communication protocol)
            # For example, you might use socket programming or a file transfer protocol like FTP

            # Move the sent file to the share_received folder
            shutil.move(file_path, os.path.join(share_received_dir, file_name))

    print("All share files sent.")

def receive_share_files():
    """
    Receive share files into 'share_received' folder.
    """
    share_received_dir = 'share_received'

    # Ensure the share_received folder exists
    if not os.path.exists(share_received_dir):
        os.makedirs(share_received_dir)

    # Receive share files (implementation depends on the specific communication protocol)
    # For example, if you're using socket programming, you'd listen for incoming files

    print("All share files received.")