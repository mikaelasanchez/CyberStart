#
# Find the valid png file in the /tmp directory. Using magic bytes.
# The code is hidden in this file.
#

import imghdr
import os

# For each file in /tmp,
for files in os.listdir("/tmp"):

  # If the type of file is a png,
  if (imghdr.what("/tmp/"+files) == 'png'):

    # Print the files found, open and print the contents
    print("Found it: "+files)
    pngfile = open("/tmp/"+files, "r")
    print pngfile.read()
    break