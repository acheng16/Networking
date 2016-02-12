import sys, os

#gets filename from command line arguements
filename = sys.argv[1];
dir = "recv/";

#makes sub-directory if does not exist
if not os.path.exists(dir):
    os.makedirs(dir);
newFilename = dir+filename;

#opens the original file
try:
    originalFile = open(filename,"rb");
except IOError as e:
    print ('The file with this filename does not exist.');

#creates/opens new file
newFile = open(newFilename,"wb+");

#loops and reads and writes 960 bytes at a time to new file
byte = originalFile.read(960);
while byte:
    newFile.write(byte);
    byte = originalFile.read(960);

#closes both files
newFile.close();
originalFile.close();
