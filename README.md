# Python Chat Application

** Collaborated with Sofia Azam and Marian Sousan **

## How it works
This is a chat application to connect two devices and allows them to communicate by sending messages back and forth. The server and client both provide their usernames, and the IP address/port number they wish to communicate over. Then they can send messages to each other, one at a time, until one of them sends a message containing the exit keyword ('end') to terminate the program.

## How to run on Visual Studio Code
1. Run server.py script by clicking the "Run python file" button in the top right
2. Run client.py script by clicking Run > Run without debugging

## How to use
1. After running the server script, enter an IP address (or press enter for 'localhost'), a port number (or press enter for port 8000), and the server's username
    Note: the server side will pause after this step. At this point, switch over to the client side, run the script, and repeat step 1 on the client side.
2. The client will be prompted to send a message to the server. Type in a message and press enter.
3. The server will then be prompted to send a message to the client. Type in a message and press enter.
4. Repeat steps 2 and 3 until you wish to end the chat application. To do so, on either the client or server side (both will work) type end and press enter.
