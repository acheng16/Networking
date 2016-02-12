# Name: Andrew Cheng

# client program

import socket # For implementing sockets
import sys  # For exit and command line arguments
import os.path # For checking folders and files
import errno # For handling errors

if len(sys.argv) != 4:  # Check if the number of command line arguments are correct
	print ('Invalid # of arguments. Use format: "ftpc.py <remote-IP> <remote-port> <local-file-to-transfer>"')
	sys.exit();

HOST = sys.argv[1]    		     # server host
PORT = int(sys.argv[2])              # server port
filename = sys.argv[3]  	     # Filename

# create TCP socket, error if failed
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
except (socket.error, msg):
	print ('Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message: ' + msg[1])
	sys.exit();
print ('Socket Created') 

# Connect to host
s.connect((HOST, PORT))  
print ('Socket connected to ' + HOST + ' on port ' + str(PORT)) 

# Check if file exists
if not os.path.exists(filename):
	print ('Error: File DNE. Enter valid filename.')
	sys.exit();

size = os.path.getsize(filename)
filename = filename.rjust(20)  		# the 20 byte filename

byte_size = size.to_bytes(4, byteorder = 'big')		# Convert size to bytes in Big Endian
byte_filename = filename.encode()	# Encode filename to bytes
s.send(byte_size)  			# Send size of file in bytes
print ('File size sent.')

s.send(byte_filename)  # Send filename
print ('File name sent.')
readFile = open(filename.lstrip(), 'rb')	# Open file in binary

# read bytes until EoF
data = readFile.read(960)
while data != b"":  
	s.send(data)
	data = readFile.read(960)
readFile.close() # Close file
s.close() # Close socket

print ("Transfer Complete. Socket Closed.")

