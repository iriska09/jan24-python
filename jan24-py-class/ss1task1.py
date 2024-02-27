def reverse (string) :
    string = string [::-1]
    return string 
s = "Hello World!"
print ("The original string is : ", end='')
print (s)
print ("The reversed string (using extended slice sytax) is :", end='')
print (reverse(s))
