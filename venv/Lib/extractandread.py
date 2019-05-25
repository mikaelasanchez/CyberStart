#
# Sample Alien Zip file found at /tmp/alien-zip-2092.zip is password protected
# We have worked out they are using three digit code
# Brute force the Zip file to extract to /tmp
#
# Note: The script can timeout

import zipfile
import itertools
import time

# Method to extract file and return a boolean
def extractFile(zfile, passw):

    # Try to extract the file into /tmp
    # If there's an exception, return false
    try:
        zfile.extractall("/tmp", pwd=passw)
        return True
    except:
        return False

# Set file and digits to brute force
zipfile = zipfile.ZipFile("/tmp/alien-zip-2092.zip")
digits = "1234567890"

# For every possible combination of 3 digits,
for c in itertools.product(digits, repeat=3):
    print("Trying: " + str(c))

    # Try to extract the file and if true, say code is found
    if extractFile(zipfile, c):
        print("Code found!: " + str(c))
        break

# Try to open and read the text file and print to console
txtfile = open("/tmp/alien-zip-2092.txt", "r")
contents = txtfile.read()
print(contents)
txtfile.close()