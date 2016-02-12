# Name: Andrew Cheng

# client program

import time # for sleep
import socket # For implementing sockets
import sys  # For exit and command line arguments
import os.path # For checking folders and files
import errno # For handling errors

if len(sys.argv) != 5:  # Check if the number of command line arguments are correct
	print ('Invalid # of arguments. Use format: "ftpc.py <remote-IP> <remote-port> <troll-local-port> <local-file-to-transfer>"')
	sys.exit();

HOST = sys.argv[1]    		     # client server host
PORT = int(sys.argv[2])              # client server port
TROLLPORT = int(sys.argv[3])	     # troll port
filename = sys.argv[4]  	     # Filename

HOSTIP = socket.gethostbyname(socket.getfqdn(HOST))	# inputed HOST, grab the IP
HOSTIP_encoded = socket.inet_aton(HOSTIP)		# IP converted to Bytes
PORT_encoded = PORT.to_bytes(2, byteorder='big')	# Port converted to Bytes

# create UDP socket, error if failed
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
except (socket.error, msg):
	print ('Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message: ' + msg[1])
	sys.exit();
print ('Socket Created') 

# attempt to bind the socket
try:
	s.bind((socket.gethostname(),9611))
except (socket.error, msg):
	print('Failed to bind the socket to server\'s hostname and port 9611')
	sys.exit()
print ('Socket binded to 9611')

# Check if file exists
if not os.path.exists(filename):
	print ('Error: File DNE. Enter valid filename.')
	sys.exit();

size = os.path.getsize(filename)	# gets the size of file
filename = filename.rjust(20)  		# the 20 byte filename

flag = 1	# Set flag
flag_encoded = flag.to_bytes(1, byteorder = 'big')	# flag to bytes

byte_size = size.to_bytes(4, byteorder = 'big')		# Convert size to bytes in Big Endian
byte_filename = filename.encode()	# Encode filename to bytes

try:
	s.sendto(HOSTIP_encoded+PORT_encoded+flag_encoded+byte_size, ('', TROLLPORT))  			# Send size of file in bytes
	print ('File size sent.')
except (socket.error, msg):
	print('Failed to send size of file to TROLL: '+ str(msg[0]) + ' , Error message: ' + msg[1])
	sys.exit();

flag = 2	#Set flag
flag_encoded = flag.to_bytes(1, byteorder = 'big') 	# flag to bytes

s.sendto(HOSTIP_encoded+PORT_encoded+flag_encoded+byte_filename, ('',TROLLPORT))  # Send filename
print ('File name sent.')
readFile = open(filename.lstrip(), 'rb')	# Open file in binary

flag = 3	#Set flag
flag_encoded = flag.to_bytes(1, byteorder = 'big')	# flag to bytes

# read bytes until EoF
data = readFile.read(960)
while data != b"":  
	print("Sending file data")
	s.sendto(HOSTIP_encoded+PORT_encoded+flag_encoded+data, ('',TROLLPORT)) # Keep sending data until all data is sent
	time.sleep(.01)		# sleep to prevent overloading of buffer
	data = readFile.read(960)
s.sendto(HOSTIP_encoded+PORT_encoded+flag_encoded+data, ('',TROLLPORT))
readFile.close() # Close file
s.close() # Close socket

print ("Transfer Complete. Socket Closed.")

