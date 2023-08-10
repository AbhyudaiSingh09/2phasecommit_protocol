from uploadconfig import ConfigLoader
from sendmessage import MessageSender

config_loader=ConfigLoader()
message_sender=MessageSender()

#configuration data
master_config = config_loader.upload_master_config()
master_ip=master_config['ip']
master_port = master_config['port']
node_p1_config = config_loader.upload_config_Node_P1()
node_p1_ip= node_p1_config['ip']
node_p1_port= node_p1_config['port']
node_p2_config = config_loader.upload_config_Node_P2()
node_p2_ip=node_p2_config['ip']
node_p2_port=node_p2_config['port']


class Client:
    def __init__(self,config):
        self.ip = config['ip']
        self.port= config['port']


    def sendmessage_tonode(self,node,message):
        if node.lower() == 'node1': 
            message_sender.send_message(master_ip,master_port,message)
            message_sender.send_message(node_p1_ip,node_p1_port,message)

        if node.lower() == 'node2': 
            message_sender.send_message(master_ip,master_port,message)
            message_sender.send_message(node_p2_ip,node_p2_port,message)


    def check_input(self,message):
        if message.lower()=='commit':
            message_sender.send_message(master_ip,master_port,message)
            message_sender.send_message(node_p1_ip,node_p1_port,message)
            message_sender.send_message(node_p2_ip,node_p2_port,message)
        else: 
            node = input("Enter the node (node1 or node2): ")
            self.sendmessage_tonode(node,message)







if __name__ == "__main__":
    client_config = config_loader.upload_client_config()
    print(f"Current Client config:{client_config}")
    client =Client(client_config)
    message = input("Enter message: ")
    client.check_input(message)