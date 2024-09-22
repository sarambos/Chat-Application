import socket as s

try: # Make sure the user gives a valid IP address
    server_ip = input("Enter an IP address (press enter for localhost): ")
    if server_ip == "":
        server_ip = "localhost"
except: # Exit the program if IP address is invalid
    print("Invalid IP address.")
    quit()

try: # Make sure the user gives a valid port number
    server_port = input("Enter a port number (press enter for a default port): ")
    if server_port == "":
        server_port = 8000
except: # Exit the program if the port number is invalid
    print("Invalid port number.")
    quit()

# Get the servers username
username = input("Enter your username: ")

# Set up the server socket
server_socket = s.socket(s.AF_INET, s.SOCK_STREAM)

try: # Make sure the bind function works when binding the server IP and port number
    server_socket.bind((server_ip, int(server_port)))
except: # Exit the program if the bind function fails
    print("Could not bind IP address and port number.")
    server_socket.close()
    quit()

# Open the socket for connections
server_socket.listen(1)

try: # Make sure the server and client connect
    connection_socket, client_address = server_socket.accept()
except: # Exit the program if the connection fails
    print("Connection error.")
    server_socket.close()
    quit()

print("Type 'end' to end the conversation.")
while True:
    try: # Make sure the client message comes through
        client_message = connection_socket.recv(2048).decode()
    except: # Exit the program if the client's message does not go through
        print("Could not receive message from client.")
        connection_socket.close()
        quit()

    if client_message == "end": # Check if the client is trying to end the chat
        # Break out of the loop and exit the program
        break
    
    # Print the message to the screen
    print(client_message)

    # Get the users' response to the client
    server_message = input(username + ": ")
    
    if server_message == "end": # Check if the user is trying to end the chat
        # Break out of the loop and exit the program
        connection_socket.send("end".encode())
        break

    try: # Make sure the users' message gets to the client
        connection_socket.send((username + ": " + server_message).encode())
    except: # Exit the program if the users' message does not go through
        print("Error sending message.")
        connection_socket.close()
        quit()
# Close the socket after breaking out of the while loop
connection_socket.close()