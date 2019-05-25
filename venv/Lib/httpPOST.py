#
# Tweet bot API listening at http://127.0.0.1:8082.
# GET / returns basic info about api. POST / with x-api-key:tweetbotkeyv1
# and data with user tweetbotuser and status-update of alientest
#


import urllib2
import urllib

request = urllib2.Request("http://127.0.0.1:8082")
response = urllib2.urlopen(request)
html = response.read()
print(html)

data = urllib.urlencode({'user' : 'tweetbotuser', 'status-update'  : 'alientest'})
request = urllib2.Request("http://127.0.0.1:8082", headers={'x-api-key':'tweetbotkeyv1'}, data=data)
response = urllib2.urlopen(request)
print response.read()

'''
<html><body><h1>I am TweetBot!</h1><p>Post with header x-api-key</p><<p>Parameters should include user and status-update.</p>/body></html>
{"success": "true", "message":"Well done.", "flag":"Well done the flag is: DXDAGMLVCWX "}

'''