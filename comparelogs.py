from logs import commit_log


# Create a dictionary to store logs for each node
master_transaction_ids = {}
node1_transaction_ids= set()
node2_transaction_ids=set()
node1_missing_ids=set()
node2_missing_ids= set()
update_node1_logs_list=[]
update_node2_logs_list=[]

def read__updatenode1logs():
    with open('./logs/master_commit.log', 'r') as log_file:
        for line in log_file:
            parts = line.strip().split('|')
            if parts[0]== None:
                pass
            node_id = parts[0]
            if node_id not in master_transaction_ids:
                master_transaction_ids[node_id] = []
            # print(f"node_logs[node_id]:{node_logs[node_id]}")
            if len(parts) > 2:
                master_transaction_ids[node_id].append(parts[1:])
            else:
                master_transaction_ids[node_id].append(parts[1])
    with open('./logs/node1_commit.log', 'r') as log_file:
        for line in log_file:
            parts = line.strip().split('|')
            if len(parts) < 2:
                continue 
            transaction_id = parts[0]
            node1_transaction_ids.add(transaction_id)
    for node_id in master_transaction_ids:
        if node_id not in node1_transaction_ids:
            node1_missing_ids.add(node_id)
    for node1_missing_id in node1_missing_ids:
        if node1_missing_id in master_transaction_ids:
            missing_log = master_transaction_ids[node1_missing_id]
            update_node1_logs_list.append((node1_missing_id, missing_log))
            commit_log('node1',update_node1_logs_list)




def read__updatenode2logs():
    with open('./logs/master_commit.log', 'r') as log_file:
        for line in log_file:
            parts = line.strip().split('|')
            if parts[0]== None:
                pass
            node_id = parts[0]
            if node_id not in master_transaction_ids:
                master_transaction_ids[node_id] = []
            # print(f"node_logs[node_id]:{node_logs[node_id]}")
            if len(parts) > 2:
                master_transaction_ids[node_id].append(parts[1:])
            else:
                master_transaction_ids[node_id].append(parts[1])
    with open('./logs/node2_commit.log', 'r') as log_file:
        for line in log_file:
            parts = line.strip().split('|')
            if len(parts) < 2:
                continue 
            transaction_id = parts[0]
            node2_transaction_ids.add(transaction_id)
    for node_id in master_transaction_ids:
        if node_id not in node2_transaction_ids:
            node2_missing_ids.add(node_id)
    for node2_missing_id in node2_missing_ids:
        if node2_missing_id in master_transaction_ids:
            missing_log = master_transaction_ids[node2_missing_id]
            update_node2_logs_list.append((node2_missing_id, missing_log))
            commit_log('node1',update_node2_logs_list)



