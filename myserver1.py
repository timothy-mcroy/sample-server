import socket

HOST, PORT = '', 8888

#socket.AF_INET
# Create a socket with the Address Family of InterNET
#socket.SOCK_STREAM
# Use a protocol that supports streaming (In this case, TCP)
# socket.SOCK_DGRAM for UDP
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#These are things that we haven't really learned about
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#Bind the host and port
# '' gives the OS default, which is 
listen_socket.bind((HOST, PORT))

listen_socket.listen(5)

print 'Serving HTTP on port %s' % PORT

while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print request

    http_response = """\
HTTP/1.1 200 OK

Hello World!
"""
    client_connection.sendall(http_response +str(client_address)+ request.split('\n')[-1])
    client_connection.close()
