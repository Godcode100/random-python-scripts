#Network basics using socket programming module
#The socket module exposes all the necessary pieces to write Tcp and Udp client and server for writing low level network applications.
#We will also cover the implementation of a reverse shell using socket module and implement secure sockets with TLS
#sOCKETProgramming refers to an abstract principle by which 2 programs can share any data stream by using an API for different protocols available 
#in the internet TCP/IP stack typically supported by all operating systems


# UNDERSTANDING THE SOCKET PACKAGE FOR REQUESTS
#Sockets allow us to leverage the capabilities of an OS to communicate/nteract with a network
#You may regard sockets as the main point to point channel of communication between clients and server

#A socket address for a network consists of an IP Address and  port number
#Sockets are internal endpoints for sending and receiving data within a node on a computer
#A socket is defined by local and remote IP addresses and ports and a transport protocol
# We use the socket.socket() to create a socket in Python