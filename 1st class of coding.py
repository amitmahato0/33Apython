a =('what\'s up')    #use backslash to use inverted comma inside inverted same no of comma
print(a)

print("Hello Python")       
print("\tworld")          #use \t to make 8 space in another line

print("\tworld".expandtabs(tabsize=16))     #to extend as required

print("Hello\b python")      #use \b to erase one item

print("Hello\n World")       #to produce ouput in different line   #use \n

print(r"Hello\n Ameet")      #use r infront to disable the effects of \t \n \b.  
                             #r is raw string.

print("Hello\\Colz")        #use twice time backslash to print backslash
                            #for 1 backslash  use 2 backslash ,  for 2 =4 ,  for 3 = 6

a = "Amit"
b = a.replace("i","e")                 #to replace
print(b)                   

a = "Sumit"
b = a.replace("","")            
print(len(b))                         #no change in length

a = " Conventry "
b = a.lstrip                       #lstrip & rstrip     #bujina   #padna baaki xa
print(b)

import re                    #to import replace function in python

a = "Hello "
b =re.sub(" ","",a)                         #subsituting ''   ''    by '' ''
print(b)                                    #subsituting gap by non gap

a = "Hello"
b = 'P'+a                             #adding P 
print(b)

a = "Hello"
print(a[0:4])                    
print(a[-1:-3])                  #ranging and slicing

a = "Amt"
b = a[0:2]+ 'i' + a[2:3]
print(b)

a.lower    #for changing into lower case
a.upper     #for changing into uppercase
a.swapcase  #for changing upper into lower and lower into upper case

a.title        #for making 1st letter of every word capital
a.capitalize   #for making 1st letter capital

a = "Soft"
print(a.lower())
print(a.upper())
print(a.swapcase())


a ="Hi22"
print(a.isalnum())            #to check is it belong to alphabet and number
print(a.isalpha())            #to check is it belong to alphabet
print(a.isdigit())            #to check is it belong to number

print(a.isidentifier())           #to check is it identifier or not
print(a.isprintable())            #to check is it printable or not
print(a.isspace())                #to check it is whitespace or not
                                #isspace : true result if there is blank string
                                        #false if there is any data in string

a ="1abc"
b = a.isidentifier()
print(b)

a= "Hello"
b= a.zfill(7)         #to fill upto 7 characters
print(b)

a="Hello"
b=a.count('l')            #couting the number of L  character in Hello string
print(b)

