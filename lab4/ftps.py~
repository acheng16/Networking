# Name: Andrew Cheng.620

# Server Program

import socket
import sys
import os.path

if len(sys.argv) != 3:  # Check if the number of command line arguments are correct
	print('Invalid # of arguments. Use format: "ftpc.py <local-port> <troll-local-port>"')
	sys.exit();

HOST = socket.gethostname()             # host
PORT = int(sys.argv[1])              # Arbitrary non-privileged port
TROLLPORT = int(sys.argv[2])

# Create socket, print error if failure
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
	print ('Failed to create socket')
	sys.exit()

print ('Socket Created')  # Let user know socket was successfully created
print ('The host is : %s'%HOST) # Print Host IP

# Bind socket, print error if failed
try:
	s.bind((HOST,PORT))
	print ('Socket bind complete')
except socket.error:
	print('Failed to bind socket to host %s and port number %d' %(HOST,PORT))
	sys.exit()

# let user know socket is listening
print ('Awaiting packets...')

duplicate_data = b""
bytesRead = 0

while 1:
	data, addr = s.recvfrom(1000)		# receive 1000 bytes
	print ('Recieving from' , addr)
	clientIP_encoded = data[0:4]		# by def IP first 4 bytes
	clientPORT_encoded = data[4:6]		# by def PORT next 2 bytes
	ACK_encoded = data[7:8]
	if duplicate_data == data: # if data is duplicate send back ACK
		s.sendto(clientIP_encoded+clientPORT_encoded+ACK_encoded, ("",TROLLPORT)) # send back ACK
		print ("Duplicate Packet")
	else:
		duplicate_data = data
		s.sendto(clientIP_encoded+clientPORT_encoded+ACK_encoded, ("",TROLLPORT)) # send back ACK
		if (int.from_bytes(data[6:7], byteorder='big') == 1):	# flag for size
			byte_size = data[8:len(data)]	# after byte 7 is the actual data transmitted
			size = int.from_bytes(byte_size, byteorder='big') # byte to int
			print ('Size of file: ', size)
		if (int.from_bytes(data[6:7], byteorder='big') == 2):	# flag for filename
			byte_filename = data[8:len(data)]
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

		if (int.from_bytes(data[6:7], byteorder='big') == 3):  # flag for actual data
			data = data[8:len(data)]
			writeFile.write(data)
		
			if len(data) < 960:		# stops execution of loop when we are at EOF
				break

writeFile.close()  # Close file
s.close() # Close socket
print ('Transfer Complete. Socket Closed.')
