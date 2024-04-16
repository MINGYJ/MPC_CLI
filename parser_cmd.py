from urllib.parse import urlparse
class parser_cmd:
    def __init__(self,command) -> None:
        self.command=command
        self.code=0
        pass
    
    def host_port(command):
        parsed_url=urlparse(command)
        if(parsed_url.scheme==''):
            #print("No scheme found, please enter a valid URL with hostname and port")
            return None
        else:
            return parsed_url
        
    def stats_type(command):
        command=command.strip()
        parsed_stat=command.split(":")
        if len(parsed_stat)!=2 or parser_cmd.is_float(parsed_stat[1])==False:
            #print("Invalid format, please enter in the format: type:value")
            return None
        else:
            parsed_stat[0]=parsed_stat[0].lower()
            parsed_stat[1]=parsed_stat[1].strip()
            parsed_stat[1]=float(parsed_stat[1])
            return ({parsed_stat[0]:parsed_stat[1]})
        
    def is_float(string):
        try:
            float(string)
            return True
        except ValueError:
            return False