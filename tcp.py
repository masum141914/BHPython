import socket  # Import the socket module to enable network communication

# Define the target server (Google) and the port number
# Port 80 is the default port for HTTP
target_host = "www.google.com"
target_port = 80

# Create a socket object
# AF_INET  -> Use IPv4 addressing
# SOCK_STREAM -> Use TCP (reliable, connection-based protocol)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#print(socket.socket(socket.AF_INET, socket.SOCK_STREAM))

# Connect the socket to the target host and port
# This establishes a TCP connection to www.google.com on port 80
client.connect((target_host, target_port))

# Send an HTTP GET request to the server
# b"" means the data is sent as bytes (required for sockets)
# \r\n represents a new line in HTTP
# The empty line at the end (\r\n\r\n) tells the server the request is finished
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# Receive data from the server
# 4096 is the maximum number of bytes to receive at one time
response = client.recv(4096)

# Decode the received bytes into a readable string and print it
print(response.decode())

# Close the socket connection
# This releases network resources
client.close()
