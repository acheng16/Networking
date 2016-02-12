# Name: Andrew Cheng.620

# Server Program

import socket
import sys
import os.path

if len(sys.argv) != 2:  # Check if the number of command line arguments are correct
	print('Invalid # of arguments. Use format: "ftpc.py <remote-port>"')
	sys.exit();

HOST = ""              # Symbolic name meaning all available interfaces
PORT = int(sys.argv[1])              # Arbitrary non-privileged port

# Create socket, print error if failure
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
	print ('Failed to create socket')
	sys.exit()

print ('Socket Created')  # Let user know socket was successfully created
print (HOST) # Print Host IP

# Bind socket, print error if failed
try:
	s.bind((HOST, PORT))
except (socket.error , msg):
	print ('Bind failed. Error Code: ' + str(msg[0]) + ' Message ' + msg[1])
	sys.exit()

# Let user know socket bind was successfully
print ('Socket bind complete')

#allow one connection
s.listen(1) 
print ('Socket now listening')

# let user know connected address
conn, addr = s.accept()
print ('Connected by', addr)

# first 4 byte is size
socket.MSG_WAITALL = 4;
byte_size = conn.recv(1024, socket.MSG_WAITALL)
size = int.from_bytes(byte_size, byteorder='big') # byte to int
print ('Size of file: ', size)

# next 20 bytes is filename
socket.MSG_WAITALL = 20;
byte_filename = conn.recv(1024, socket.MSG_WAITALL)
filename = byte_filename.decode()
# support for files not in same directory
if filename.rfind('/'):
	index = filename.rfind('/')
filename = filename[index+1:]
filename = filename.lstrip() # byte to string & strip zero
print ('Name of file: ', filename)

# make subdir if not exist
subDir = 'recv/'
try:
	if not os.path.exists(subDir):
		os.makedirs(subDir)
except (OSError, IOError):
	print ('Error: could not create directory recv/')
	sys.exit()

# open file to be writing
writeFile = open(subDir + filename, 'wb')

socket.MSG_WAITALL = 0;  # Read until finish no more waiting
bytesRead = 0
while bytesRead < size:  # Keep recieving until all bytes been write
	data = conn.recv(960)
	bytesRead += len(data)
	writeFile.write(data)

writeFile.close()  # Close file
conn.close() # Close socket
print ('Transfer Complete. Socket Closed.')
