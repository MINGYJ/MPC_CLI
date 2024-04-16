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