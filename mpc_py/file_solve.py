import json
import os
from .server_func import server_func
from .merge import merge

# Parameter eg. command='age',party_size=3,stats=20
def compute_sum(command,party_size,stats):
    """
    Compute the sum of statistics for a given command and party size.
    """
    # Run the numerical data through server_func to calculate the sum
    sum_result = server_func.sum(stats)

    # Save the result shares in files
    sum_data = {
        'shares': sum_result,
        'command': command,
        'party_size': party_size
    }

    sum_file_name = f"SUM_{command}_{party_size}.txt"
    with open(os.path.join('share_to_send', sum_file_name), 'w') as send_file:
        json.dump(sum_data, send_file)

    with open(os.path.join('share_received', sum_file_name), 'w') as receive_file:
        json.dump(sum_data, receive_file)

    return sum_result

def compute_average(command, party_size, stats):
    """
    Compute the average of statistics for a given command and party size.
    """
    average_result = server_func.average(stats)
    average_data = {
        'shares': average_result,
        'command': command,
        'party_size': party_size
    }
    average_file_name = f"{command}_{party_size}.txt"
    with open(os.path.join('share_to_send', average_file_name), 'w') as send_file:
        json.dump(average_data, send_file)

    with open(os.path.join('share_received', average_file_name), 'w') as receive_file:
        json.dump(average_data, receive_file)

    return average_result

def compute_max(command, party_size, stats):
    """
    Compute the maximum of statistics for a given command and party size.
    """
    max_result = server_func.max(stats)
    max_data = {
        'shares': max_result,
        'command': command,
        'party_size': party_size
    }
    max_file_name = f"{command}_{party_size}.txt"
    with open(os.path.join('share_to_send', max_file_name), 'w') as send_file:
        json.dump(max_data, send_file)

    with open(os.path.join('share_received', max_file_name), 'w') as receive_file:
        json.dump(max_data, receive_file)

    return max_result

def compute_min(command, party_size, stats):
    """
    Compute the minimum of statistics for a given command and party size.
    """
    min_result = server_func.min(stats)
    min_data = {
        'shares': min_result,
        'command': command,
        'party_size': party_size
    }
    min_file_name = f"{command}_{party_size}.txt"
    with open(os.path.join('share_to_send', min_file_name), 'w') as send_file:
        json.dump(min_data, send_file)

    with open(os.path.join('share_received', min_file_name), 'w') as receive_file:
        json.dump(min_data, receive_file)

    return min_result