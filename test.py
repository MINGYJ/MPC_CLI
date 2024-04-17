class host_port:
    host_port={'hostname':None,'port':None}
    def __init__(self,hostname,port) -> None:
        self.host_port={'hostname':hostname,'port':port}
        
    def __getitem__(self, __name: str):
        return self.host_port[__name]

pp=host_port("localhost",8080)
print(pp.hostname)