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

# Set up the client socket
client_socket = s.socket(s.AF_INET, s.SOCK_STREAM)

try: # Make sure the server and client connect
    client_socket.connect((server_ip, int(server_port)))
except: # Exit the program if the connection fails
    print("Connection error.")
    client_socket.close()
    quit()

print("Type 'end' to end the conversation.")
while True:
    # Get the users' message to the server
    client_message = input(username + ": ")
    
    if client_message == "end": # Check if the user is trying to end the chat
        # Break out of the loop and exit the program
        client_socket.send("end".encode())
        break
    
    try: # Make sure the users' message goes through
        client_socket.send((username + ": " + client_message).encode())
    except: # Exit the program if the users' message does not go through
        print("Error sending message.")
        client_socket.close()
        quit()

    try: # Make sure the users' message gets to the server
        server_message = client_socket.recv(2048)
    except: # Exit the program if the users' message does not go through
        print("Could not receive message from server.")
        client_socket.close()
        quit()
    
    if server_message == "end": # Check if the server is trying to end the chat
        # Break out of the loop and exit the program
        break

    # Print the message to the screen
    print(server_message.decode())
# Close the socket after breaking out of the while loop
client_socket.close()