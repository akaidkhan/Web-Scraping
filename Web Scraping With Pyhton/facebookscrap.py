import http.cookiejar
import urllib.request
import requests
import bs4

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor)

urllib.request.install_opener(opener)

authentication_url = "http://mbasic.facebook.com/login.php"

payload = {
'email':"brainkhan0123@gmail.com",
'pass' : ""

}

data = urllib.parse.urlencode(payload).encode('utf-8')
req = urllib.request.Request(authentication_url, data)
resp = urllib.request.urlopen(req)
content = resp.read()
print(content)