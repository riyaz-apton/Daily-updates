#Requests library is one of the important aspects of Python
#for making HTTP requests to a specified URL
import requests
#The GET method is used to retrieve information from the given server using
#a given URI
# Making a GET request
r = requests.get('https://github.com/Apton-riyazS/daily-update') 
# check status code for response received
# success code - 200
print(r)
  
# print content of request
print(r.content)
