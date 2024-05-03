import os

class server_func:

    path='../share_to_send/'

    def __init__(self):
        pass

    def add(self,range):
        share_add=0
        inDir = os.listdir(self.path)
        for file_name in inDir:
            entire_path = os.path.join(self.path, file_name)
            with open(entire_path, 'r') as file:
                for line in file:
                    try:
                        share_add += int(line.strip())
                    except Exception as e:
                        print("Error calculating sum.")
        return share_add
    
    def average(self, range):
        share_avg=0
        count=0
        inDir = os.listdir(self.path)
        for file_name in inDir:
            entire_path = os.path.join(self.path, file_name)
            with open(entire_path, 'r') as file:
                for line in file:
                    try:
                        share_avg += float(line.strip())
                        count += 1
                    except Exception as e:
                        print("Error calculating average.")
        return share_avg/count if count else 0
        
    def max(self, range):
        max_value = None
        inDir = os.listdir(self.path)
        for file_name in inDir:
            entire_path = os.path.join(self.path, file_name)
            with open(entire_path, 'r') as file:
                for line in file:
                    try:
                        max_share = float(line.strip())
                        if max_share > max_value or max_value is None:
                            max_value = max_share
                    except Exception as e:
                        print("Error determining maximum value.")
        return max_value 
    
    def min(self, range):
        min_value = None
        inDir = os.listdir(self.path)
        for file_name in inDir:
            entire_path = os.path.join(self.path, file_name)
            with open(entire_path, 'r') as file:
                for line in file:
                    try:
                        min_share = float(line.strip())
                        if min_value < min_share or min_value is None:
                            min_value = min_share
                    except Exception as e:
                        print("Error determining minimum value.")
        return min_value


                