

```markdown
# Two-Phase Commit Fault Tolerance Protocol Implementation

This repository contains a Python implementation of the Two-Phase Commit (2PC) protocol. The 2PC protocol is a distributed transaction protocol that ensures all nodes involved in a distributed transaction either commit or abort the transaction consistently.

## Overview

This project demonstrates the fundamental concepts of the 2PC protocol and provides a practical example of how it can be implemented in Python. The repository includes components for the master node and two participant nodes, along with utilities to handle client connections, message processing, and logging.

## Getting Started

To run the 2PC protocol on your local machine, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/Axs7941/2phasecommit_protocol.git
   cd 2phasecommit_protocol
   ```

2. Set up a virtual environment (optional but recommended):
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Configure the nodes and master by updating the configuration files in the `config` directory.

5. Run the Master node:
   ```sh
   python master.py
   ```

6. Run Node 1 and Node 2 in separate terminal windows:
   ```sh
   python nodes.py node1
   python nodes.py node2
   ```

7. Observe the console output to see the 2PC protocol in action.

## Components

- `master.py`: Implements the Master node responsible for coordinating transactions.
- `nodes.py`: Implements Node 1 and Node 2 that participate in distributed transactions.
- `handleclient.py`: Handles client connections and messages for Node 1 and Node 2.
- `messagehandler.py`: Defines the MessageHandler class for message processing and coordination.
- `sendmessage.py`: Provides functionality to send messages between nodes.
- `uploadconfig.py`: Loads configuration settings for nodes and the master from configuration files.
- `logs.py`: Implements logging functions to record transaction details.

![Two-Phase Commit Process](https://github.com/Axs7941/2phasecommit_protocol/raw/master/public/2phasecommit.png)

## Contributing

Contributions are welcome! If you find bugs, have suggestions for improvements, or want to add new features, feel free to open issues or submit pull requests.
