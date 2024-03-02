for else and while else is gonna run when the loop is finished 

for i in range(5):
    print(i)
else:
    print("The loop is finished")


#break ---> terminates the loop ---->
for i in range (10):
    if i == 4:
        break
#continue---> skips the some part of loop and ----->
for i in range (10):
    if i == 4:
        continue
    print(i)
else:
    print("The loops is stopped ")
  ####odd#### continue####numbers------>
  for i in range (10):
    if i % 2 == 1:
        continue
    print(i)
else:
    print("The loops is stopped ")
    ### pass ### is not executes the code  keeps until you write a code 
    for i in range 
    pass 
    while true:
        pass

###task 1
for i in range(1,4):
    for x in range(1,4):
        for j in range(1,4):
                print(i,x,j)
###holds####
   lst = [] 
   print(type(lst))            list starts with squere brackets 
jan24_names = ["Aiperi","Khusrav","Fatima","Yrys","Myroslav","Dastan"]
print(jan24_names [-1] [0:3]) #####3output is DAS


#######listing the names
jan24_names = ["Aiperi","Khusrav","Fatima","Yrys","Myroslav","Dastan"]
for name in jan24_names:
    print(name[:-1])


###reversing ###t he list 
jan24_names = ["Aiperi","Khusrav","Fatima","Yrys","Myroslav","Dastan"]
for name in jan24_names:
    print(name[::-1])
numbers = [10, 10.4, 90, 110, 10, 23.3]
for num in numbers:
    print (10 + 10.4 + 90 + 110 + 10 +23.3)
    sum =+numbers
######adding with insert providing insert
jan24_names = ["Aiperi","Khusrav","Fatima","Yrys","Myroslav","Dastan","Tatina"]
jan24_names.insert(4, "Esen")
print(jan24_names)
###removing the element by the index####### 
jan24_names = ["Aiperi","Khusrav","Fatima","Yrys","Myroslav","Dastan","Tatina"]
del jan24_names[-1]
print(jan24_names)

##removing with remove with actual name or element#######
jan24_names = ["Aiperi","Khusrav","Fatima","Yrys","Myroslav","Dastan","Tatina"]
jan24_names.remove("Tatina")
print(jan24_names)

####jan24_24.pop removes last one only 
#####sorts by the alphab order
jan24_names.sort(revers=True)
print (jan24_24)
######.copy#####