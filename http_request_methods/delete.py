import requests
#The DELETE method deletes the specified resource
# Making a DELETE request
r = requests.delete('https://httpbin.org/delete', data ={'key':'value'})

# check status code for response received
# success code - 200
print(r)

# print content of request
print(r.json())

