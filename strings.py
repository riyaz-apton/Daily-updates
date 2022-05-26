print("string operations")
#variable creation
s= ('hi world'' today')
#basic string operations
print (s[0])
print (s[4])
print (s+' how are you')
#strip() remove last and first white space
print(s.lower(),s.upper(),s.strip(),s.startswith('hi'),s.endswith('riyaz'))
print (s.replace('hi world','hello world'))
#returns a list of substrings separated by the given delimiter
print(s.split('delim'))
#opsite of split(), joins the elements in the given list together 
# using the string as the delimiter
print(s.join(['hi','today']))
#string slice 
s=('hello')
print(s[1:4])  #print 'ell'
print(s[:])  #print  'Hello' .
print(s[1:]) #print  ''ello' '.
print(s[-1] ) #print 'o' -- last char (1st from the end).
print(s[-4])  #print 'e' -- 4th from the end.
# %string %d -int %s-string, %f-float
 #if statement
speed =int(input("\n Enter your value: "))
print('speed: %d' %speed)
if speed >= 80:
    if speed >= 100:
        print ('danger plz stop')
    else:
        print('slow down')
else:
    print('you can go')
#while loop
a = int(input('enter a number below 50:')) 
# Condition of the while loop
while a < 50 :  
    # Find the mod of 2
    if a%2 == 0:  
        print("The number "+str(a)+" is even")
    else:
        print("The number "+str(a)+" is odd")

    # Increment `number` by 1
    a = a+1
print('***********')
print('********')
#for loop
n = 4
for i in range(0, n):
    print(i)
print('**************')
n= [6, 5, 3, 8, 4, 2, 5, 4, 11]
# variable to store the sum
sum = 0
# iterate over the list
for val in n:
    sum = sum+val
print("The sum is", sum)
print('**************')
#for loop in list
car=["hundai","swift","lumbo"]
for x in car:
    print(x)
    if x=="swift":
        break
    else:
        continue
#list operations
l=list (input('enter list of numbers for operations: '))
print(l)
#append()	adds an element to the end of the list
l.append('hello')
print(l)
print(l[1])
#change list element
l[1]= 999
#delete list element
l.remove('hello')
print(l)
del (l[1])
print(l)
#insert() method
l.extend([0,0])
l.insert(5,7)
print(l)
#count fun
print(l.count(5))
#recursive function(a function call it self)
def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
num = int(input('enter a number to find factorial: '))
print("The factorial of", num, "is", factorial(num))
#methods
#class
#oops concept