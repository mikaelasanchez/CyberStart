#
# Browse the contents of these alien directories found in /tmp/aliendir to find
# the flag
#
#

import glob

txtfiles = []
for file in glob.glob("/tmp/aliendir/*/*"):
    txtfiles.append(file)

print
txtfiles