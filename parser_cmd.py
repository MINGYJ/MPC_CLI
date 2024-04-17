# Description: This file contains the parser_cmd class which is used to parse the commands entered by the user
from color_output import *
import re


class parser_cmd:
    def __init__(self,command) -> None:
        self.command=command
        self.code=0
        pass
    
    #return parsed url with hostname and port
    #hostname = parsed_url.hostname, 
    def host_port(command):
        parsed_url=urlparse(command)
        if(parsed_url==None):
            #print("No hostname found, please enter a valid URL with hostname and port")
            return None
        else:
            return parsed_url
        
    def stats_type(command):
        command=command.strip()
        parsed_stat=command.split(":")
        if len(parsed_stat)!=2 or is_float(parsed_stat[1])==False:
            #print("Invalid format, please enter in the format: type:value")
            return None
        else:
            parsed_stat[0]=parsed_stat[0].lower()
            parsed_stat[1]=parsed_stat[1].strip()
            parsed_stat[1]=float(parsed_stat[1])
            return ({parsed_stat[0]:parsed_stat[1]})

        
    #return a list with [status code, hostname:port]
    #status code 1 is for delete, 2 is for add
    def delete_or_add_user(command):
        command=command.strip()
        if command[0:7]=="DELETE ":
            del_host=command[7:]
            del_host=parser_cmd.host_port(del_host)
            #turn the string into host_port object
            return [1,del_host]
        elif command[0:4]=="ADD ":
            add_host=command[4:]
            add_host=parser_cmd.host_port(add_host)
            return [2,add_host]
        else:
            return None
            #prRed("Invalid command, please enter DELETE hostname:port or ADD hostname:port")


    #return a list with [status code, type/type:value]
    #code 1 for delete, 2 for add, return None for invalid command
    def delete_or_add_data(command):
        command=command.strip()
        if command[0:7]=="DELETE ":
            del_type=command[7:]
            del_type=del_type.lower()
            return [1,del_type]
        elif command[0:4]=="ADD ":
            add_type=command[4:]
            add_type=parser_cmd.stats_type(add_type)
            #turn string into dictionary {type:value}
            return [2,add_type]
        else:
            return None
            


#method to parse input hostname:port
def urlparse(command):
    command=command.strip()
    cmd_list=command.split(":")
    #print(len(cmd_list))
    if len(cmd_list)!=2:
        return None
    elif is_valid_hostname(cmd_list[0])==False or cmd_list[1].isnumeric()==False:
        return None
    else:
        cmd_list[0]=cmd_list[0].strip()
        cmd_list[1]=cmd_list[1].strip()
        return host_port(cmd_list[0],cmd_list[1])

#method to check if the hostname is valid
def is_valid_hostname(hostname):
    if len(hostname) > 255:
        return False
    if hostname[-1] == ".":
        hostname = hostname[:-1] # strip exactly one dot from the right, if present
    allowed = re.compile("(?!-)[A-Z\d-]{1,63}(?<!-)$", re.IGNORECASE)
    return all(allowed.match(x) for x in hostname.split("."))

def is_float(string):
        try:
            float(string)
            return True
        except ValueError:
            return False

class host_port:
    
    def __init__(self,hostname,port) -> None:
        self.hostname=hostname
        self.port=port
        
    def hostname(self):
        return self.hostname
    def port(self):
        return self.port
    
