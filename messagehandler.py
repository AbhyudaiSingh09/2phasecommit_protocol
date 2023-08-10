import time
from sendmessage import MessageSender
from uploadconfig import ConfigLoader
from logs import commit_log

sendmessage = MessageSender()
config_loader = ConfigLoader()


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
master_message_buffer=[]
node1_buffer = []
node2_buffer = []
active_client=[]


class MessageHandler:
    def __init__(self, master_buffer, master_message_buffer, node1_buffer, node2_buffer, sendmessage, master_ip, master_port,active_client):
        self.master_buffer = master_buffer
        self.master_message_buffer = master_message_buffer
        self.node1_buffer = node1_buffer
        self.node2_buffer = node2_buffer
        self.sendmessage = sendmessage
        self.master_ip = master_ip
        self.master_port = master_port
        self.active_client= active_client


    def handle_master_message(self, message,address,transaction_id=None):
        if message.lower() == 'commit':
            time.sleep(2)  #increase the time.sleep for scenario1 
            if 'no' in self.master_buffer:
                message='abort'
                self.master_buffer.append(message)
                sendmessage.send_message(node_p1_ip,node_p1_port,message,transaction_id)
                transaction_log=f"{transaction_id}|{node_p1_ip}|abort"
                commit_log('master',transaction_log)
                print(transaction_log)
                sendmessage.send_message(node_p2_ip,node_p2_port,message,transaction_id)
                transaction_log=f"{transaction_id}|{node_p2_ip}|abort"
                commit_log('master',transaction_log)
                print(transaction_log)
            else:
                message='prepare'
                self.master_buffer.append(message)
                sendmessage.send_message(node_p1_ip,node_p1_port,message)
                transaction_log=f"{transaction_id}|{node_p1_ip}|prepare"
                commit_log('master',transaction_log)
                print(transaction_log)
                sendmessage.send_message(node_p2_ip,node_p2_port,message)
                transaction_log=f"{transaction_id}|{node_p2_ip}|prepare"
                commit_log('master',transaction_log)
                print(transaction_log)
        elif message.lower() == 'ok':
            self.active_client.append(address)
            self.master_buffer.append(message)
            time.sleep(5)
            print(f"master_buffer3:{self.master_buffer}")
            if len(self.active_client) == 2 and 'no' not in self.master_buffer:
                print(f"active_client:{self.active_client}")
                message= 'commit all'
                self.master_buffer.append(message.lower())
                transaction_log=f"{transaction_id}|{self.master_buffer}"
                print(transaction_log)
                sendmessage.send_message(node_p1_ip,node_p1_port,message,transaction_id)
                transaction_log= f"{transaction_id}|{node_p1_ip}|completed"
                commit_log('master',transaction_log)
                print(transaction_log)            
                sendmessage.send_message(node_p2_ip,node_p2_port,message,transaction_id)
                transaction_log= f"{transaction_id}|{node_p2_ip}|completed"
                commit_log('master',transaction_log)
                print(transaction_log)
                self.master_buffer.append(message)
                self.active_client.clear()
                print(f"master_buffer4:{self.master_buffer}")
            else:
                message="abort"
                self.active_client.clear()
                print(message)
                self.master_buffer.append(message)
                sendmessage.send_message(node_p1_ip,node_p1_port,message)
                transaction_log= f"{transaction_id}|{node_p1_ip}|abort"
                commit_log('master',transaction_log)
                print(transaction_log)
                sendmessage.send_message(node_p2_ip,node_p2_port,message)
                transaction_log= f"{transaction_id}|{node_p2_ip}|abort"
                commit_log('master',transaction_log)
                print(transaction_log)
                # master_commit_log(transaction_fail)
        elif message.lower() == 'no':
            self.master_buffer.append(message)
        else:
            self.master_message_buffer.append(message)



    def handle_node1_message(self, message, transaction_id):
        parts = message.split('|', 1)
        print(parts)
        if len(parts) == 2:
            transaction_id, message = parts
            print(transaction_id)
        else:
            message = message
            print(message)
            print(f"node1 received message:{message}")
        if message.lower() =='prepare':
            self.node1_buffer.append(message.lower())
            reply='ok'
            self.node1_buffer.append(reply)
            sendmessage.send_message(master_ip,master_port,reply)
        elif message.lower() =='commit all':
            self.node1_buffer.append(message.lower())
            transaction_log=f"{transaction_id}|{message}"
            print(transaction_log)
            commit_log('node1',transaction_log)
        elif message.lower() =='abort':
            self.node1_buffer.clear()
            print('Abort')
            commit_log('node1',transaction_log)
        elif message.lower() =='commit':
            self.node1_buffer.append(message.lower())
            print(f"node1 received message:{self.node1_buffer}")
            time.sleep(5)
            check_to_abort=self.node1_buffer.pop()
            if check_to_abort == 'commit':
                self.node1_buffer.clear()
                reply='no'
                sendmessage.send_message(master_ip,master_port,reply)
                commit_log('node1',transaction_log)
                print(f"Abort")
        else:
            self.node1_buffer.append(message.lower())

    def handle_node2_message(self, message, transaction_id):
        parts = message.split('|', 1)
        print(parts)
        if len(parts) == 2:
            transaction_id, message = parts
            print(transaction_id)
        else:
            message = message
            print(message)
            print(f"node2 received message:{message}")
        if message.lower() =='prepare':
            self.node1_buffer.append(message.lower())
            reply='ok'
            self.node1_buffer.append(reply)
            sendmessage.send_message(master_ip,master_port,reply)
        elif message.lower() =='commit all':
            self.node1_buffer.append(message.lower())
            transaction_log=f"{transaction_id}|{message}"
            commit_log('node2',transaction_log)
            print(transaction_log)
        elif message.lower() =='abort':
            commit_log('node3',transaction_log)
            self.node1_buffer.clear()
            print('Abort')
        elif message.lower() =='commit':
            self.node1_buffer.append(message.lower())
            print(f"node1 received message:{self.node1_buffer}")
            time.sleep(5)
            check_to_abort=self.node1_buffer.pop()
            if check_to_abort == 'commit':
                self.node1_buffer.clear()
                reply='no'
                sendmessage.send_message(master_ip,master_port,reply)
                print(f"Abort")
                commit_log('node2',transaction_log)
        else:
            self.node1_buffer.append(message.lower())