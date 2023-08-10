import socket
import threading
from handleclient import handle_message_recv_node1,handle_message_recv_node2
import argparse
from uploadconfig import ConfigLoader
from comparelogs import read__updatenode1logs,read__updatenode2logs

node_configuration =ConfigLoader()

class Node:
    def __init__(self, config):
        self.ip = config['ip']
        self.port = config['port']
        print(self.ip,self.port)

    def create_socket(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.ip, self.port))
        sock.listen()

        while True:
            connection, address = sock.accept()
            if self.ip == '127.0.0.2':
                client_thread = threading.Thread(target=handle_message_recv_node1, args=(connection, address))
                client_thread.start()
            elif self.ip == '127.0.0.3':
                client_thread = threading.Thread(target=handle_message_recv_node2, args=(connection, address))
                client_thread.start()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("node", help="Specify the node (node1 or node2)")
    args = parser.parse_args()
    node_config = None
    if args.node.lower() == "node1":
        node_config = node_configuration.upload_config_Node_P1()
        read__updatenode1logs()  
    elif args.node.lower() == "node2":
        node_config = node_configuration.upload_config_Node_P2()
        read__updatenode2logs()  
    else:
        print("Invalid node name. Please specify 'node1' or 'node2'.")
        exit()

    node = Node(node_config)
    node.create_socket()
