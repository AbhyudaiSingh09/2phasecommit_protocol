import socket


class MessageSender:
    def send_message(self, ip, port, message, transaction_id=None):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if transaction_id:
            transaction_log=f"{transaction_id}|{message}"
        else:
            transaction_log=message
        try:
            # Connect to the server
            sock.connect((ip, port))
            log_detail= f"Connected to {ip} and {port}"

            # Send the message
            sock.sendall(transaction_log.encode())
            log_detail=f"Message sent to {ip}|{port}|{transaction_log}"
            print(log_detail)
        except Exception as e:
            log_detail=(f"Error occurred: {str(e)}")
        finally:
            # Close the socket
            sock.close()



