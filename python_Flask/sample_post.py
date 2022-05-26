import requests
#POST request method requests that a web server accepts the
#data enclosed in the body of the request message, most likely for storing it
# Making a POST request
#syntax requests.post(url, params={key: value}, args)
r = requests.post('https://httpbin.org/post', data ={'key':'value'})
  
# check status code for response received
# success code - 200
print(r)
  
# print content of request
print(r.json())
