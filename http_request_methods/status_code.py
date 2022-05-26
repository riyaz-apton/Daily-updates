#After receiving and interpreting a request message, a server responds with an HTTP response message.
# The response message has a Status-Code.It is a 3-digit integer where first digit of the Status-Code defines the class of response 
# the last two digits do not have any categorization role
#1xx: Informational#2xx: Success#3xx: Redirection#4xx: Client Error#5xx: Server Error
import urllib3
http = urllib3.PoolManager()

resp = http.request('GET','http://tutorialspoint.com/robots.txt')
print (resp.data)

# get the status of the response
print (resp.status)
###################################################
##unsucessfull responce(403)
import urllib3
http = urllib3.PoolManager()

resp = http.request('GET', 'http://tutorialspoint.com/robot.txt')
print (resp.data)

# get the status of the response
print (resp.status)

