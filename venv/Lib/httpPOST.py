#
# Tweet bot API listening at http://127.0.0.1:8082.
# GET / returns basic info about api. POST / with x-api-key:tweetbotkeyv1
# and data with user tweetbotuser and status-update of alientest
#
import urllib
from urllib.request import Request, urlopen  # Python 3


req = Request("http://127.0.0.1:8082")
req.add_header('x-api-key', 'tweetbotkeyv1')
data = urllib.parse.urlencode({'user' : 'tweetbotuser', 'status-update'  : 'alientest'})
data = data.encode()
content = urlopen(req, data).read()
print(content)

```
{"success": "true", "message":"Well done.", "flag":"Well done the flag is: 1nQORVQMbfuRA1a0AUgr"}'
```
