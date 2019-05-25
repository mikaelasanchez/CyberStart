# You aren't limited to using raw sockets to make network connections.
# Python can make HTTP requests quite easily.

# Import the urllib2 module.
import urllib2

# Open the URL:
response = urllib2.urlopen("http://127.0.0.1:8080")

# Read the contents of the response:
html = response.read()
print(html)

# Make a connection to: 127.0.0.1:8080/winning and print
# the response.

response = urllib2.urlopen("http://127.0.0.1:8080/winning")
html = response.read()
print(html)