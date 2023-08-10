from uploadconfig import ConfigLoader
import socket
import threading
import sys
from handleclient import handle_client_master


master_config=ConfigLoader()




class Master:
    def __init__(self,config):
        self.ip = config['ip']
        self.port= config['port']

    def create_socket(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.ip, self.port))
        sock.listen()
        print(f"Master Initiated and listening on IP:{self.ip}|PORT{self.port}")
        sys.stdout.flush()
        while True:
            connection, address = sock.accept()
            client_thread = threading.Thread(target=handle_client_master, args=(connection, address))
            client_thread.start()



if __name__ == "__main__":
    
    master_config= master_config.upload_master_config() #start the master node 
    master = Master(master_config)
    master.create_socket()

    