str1=str(input("Please enter a four-character string for the variable chars: "))
str2=str(input("Please enter a word to insert into the middle of chars: "))
middle = int(len(str1)/2)
gm =str1[:middle:]
get =gm + str2
middle = get + str1[middle:]
print ("This is your word combination:", middle) 
("str1","str2")
