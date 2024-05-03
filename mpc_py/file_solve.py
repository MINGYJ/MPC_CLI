import json
import os

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

    # Save the shares instance into a file
    share_file_name = f"SUM_{command}_{party_size}.txt"
    share_file_path = os.path.join('share_to_send', share_file_name)
    with open(share_file_path, 'w') as share_file:
        json.dump(shares_instance.__dict__, share_file)
    
    return sum_result

def compute_average(command, party_size, stats):
    """
    Compute the average of statistics for a given command and party size.
    """

    # Run the numerical data through server_func to calculate the average
    average_result = server_func.average(stats)

    # Split the average result into shares
    shares_instance = shares(average_result, 'average', party_size, 'share_to_send')

    # Save the shares instance into a file
    share_file_name = f"AVERAGE_{command}_{party_size}.txt"
    share_file_path = os.path.join('share_to_send', share_file_name)
    with open(share_file_path, 'w') as share_file:
        json.dump(shares_instance.__dict__, share_file)

    return average_result

def compute_max(command, party_size, stats):
    """
    Compute the maximum of statistics for a given command and party size.
    """

    # Run the numerical data through server_func to calculate the maximum
    max_result = server_func.max(stats)

    # Split the max result into shares
    shares_instance = shares(max_result, 'max', party_size, 'share_to_send')

    # Save the shares instance into a file
    share_file_name = f"MAX_{command}_{party_size}.txt"
    share_file_path = os.path.join('share_to_send', share_file_name)
    with open(share_file_path, 'w') as share_file:
        json.dump(shares_instance.__dict__, share_file)

    return max_result


def compute_min(command, party_size, stats):
    """
    Compute the minimum of statistics for a given command and party size.
    """
    
    # Run the numerical data through server_func to calculate the minimum
    min_result = server_func.min(stats)

    # Split the min result into shares
    shares_instance = shares(min_result, 'min', party_size, 'share_to_send')

    # Save the shares instance into a file
    share_file_name = f"MIN_{command}_{party_size}.txt"
    share_file_path = os.path.join('share_to_send', share_file_name)
    with open(share_file_path, 'w') as share_file:
        json.dump(shares_instance.__dict__, share_file)

    return min_result