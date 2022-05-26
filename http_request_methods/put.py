#PUT method requests that the enclosed entity be stored under the supplied URI
#if the URI refers to an already existing resource, it is modified 
#if the URI does not point to an existing resource, then the server can create 
#the resource with that URI.##
# syntax requests.put(url, params={key: value}, args)
import requests

# Making a PUT request
r = requests.put('https://httpbin.org/put', data ={'key':'value'})

# check status code for response received
# success code - 200
print(r)

# print content of request
print(r.content)

