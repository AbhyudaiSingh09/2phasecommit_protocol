from messagehandler import MessageHandler
from sendmessage import MessageSender
from uploadconfig import ConfigLoader   
import uuid 



config_loader = ConfigLoader()
sendmessage = MessageSender()

master_config = config_loader.upload_master_config()
master_ip=master_config['ip']
master_port = master_config['port']
node_p1_config = config_loader.upload_config_Node_P1()
node_p1_ip= node_p1_config['ip']
node_p1_port= node_p1_config['port']
node_p2_config = config_loader.upload_config_Node_P2()
node_p2_ip=node_p2_config['ip']
node_p2_port=node_p2_config['port']
master_buffer = []
master_message_buffer = []
node1_buffer = []
node2_buffer = []
active_client=[]

message_handler = MessageHandler(
    master_buffer, master_message_buffer,node1_buffer, node2_buffer, sendmessage, master_ip, master_port,active_client
)

def handle_client_master(connection, address):
    data = connection.recv(1024)
    message = data.decode()
    transaction_id = uuid.uuid4()
    message_handler.handle_master_message(message,address, transaction_id)

def handle_message_recv_node1(connection, address):
    data = connection.recv(1024)
    messages = data.decode()
    parts = messages.split('|', 1)
    if len(parts) == 2:
        transaction_id, message = parts
    else:
        transaction_id =None
        message = messages
    message_handler.handle_node1_message(message, transaction_id)

def handle_message_recv_node2(connection, address):
    data = connection.recv(1024)
    messages = data.decode()
    parts = messages.split('|', 1)
    if len(parts) == 2:
        transaction_id, message = parts
    else:
        message = messages
        transaction_id =None
    message_handler.handle_node2_message(message, transaction_id)
