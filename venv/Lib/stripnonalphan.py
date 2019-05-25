#
# One of the agents has intercepted a file from the aliens
# The flag is hidden in large amount of non alphanumeric characters.
# The file lives at /tmp/destroymoonbase.gif
#
import re

# Open the destroymoonbase.gif file and find all alphanumeric characters
basefile = open("/tmp/destroymoonbase.gif", "r")
contents = basefile.read()
p = re.compile("[a-zA-Z0-9]")

# Join all the characters together and print to console
print ''.join(p.findall(contents))