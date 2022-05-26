#a = 5
#a='hello'+str(6)
#print(a)
#print(len(a))
################################
import sys
def main(name):
    if name=='alice' or name=='rog':
       name=name+str('!!!!!!!!')
       print('name',name)
    else:  
        name = name+'???????'
    print('name',name)
name=str(input('enter your name: '))
main(name)   
print'********************'
#########################################
a='hypper'
print( a.lower())
print(a.find('p'))
print (a[0])
########################################
print('hi %s i have %d cake'%(a,42))
########################################
## Basic string exercises
# A. donuts
# Given an int count of a number of donuts, return a string
# of the form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# So donuts(5) returns 'Number of donuts: 5'
# and donuts(23) returns 'Number of donuts: many'
#############################################
def donut(count):
    if count < 10:
        #print('number of donuts : ',int(count))
         count 
    else:
        count = 'many'
    print('number of donut is :',count)
count=int(input('enter the number of donut: '))
donut(count)
############################################
#B. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.
def bothends(s):
    if len(s) < 2:
        print('empty')
    else:
        a= s[0:2]
        b=s[-2:]
        s=a+b
        print(s)
s=str(input('enter a  letter string: '))
bothends(s)
#################################################
# C. fix_start
# Given a string s, return a string
# where all occurences of its first char have
# been changed to '*', except do not change
# the first char itself.
# e.g. 'babble' yields 'ba**le'
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s
# where all instances of stra have been replaced by strb.
########################################################
def fixstart(f):
    if len(f) < 1:
        print('empty')
    else:
        a= f[0:2]
        b=f[-2:]
        c=b.replace(b,a)
        d='*'
        f=c+d+b
        print(f)
f=str(input('enter a  letter string: '))
fixstart(f)
###########################################################
#D. MixUp
# Given strings a and b, return a single string with a and b separated
# by a space '<a> <b>', except swap the first 2 chars of each string.
# e.g.
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.
#from re import A
def mixup(a,b):
    if len(a) < 2 :
        if len(b) < 2 :
           print('sorry')
    else:
        #a=input('enter a string ')
        #b=input('enter a string ')
        m = a+b
        print(m)
a=str(input('enter a string'))
b=str (input('enter a string'))
mixup(a,b)       
################################################################## 
