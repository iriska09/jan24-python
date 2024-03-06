######## task1 ########


persons = [
    {
        "name" : "Kumo",
        "salary" :"15000",
        "age" : "23",
        "owns" : ["car","laptop","tv","monitor"],
    },
    {
        "name" : "Mike",
        "salary" :"10000",
        "age" : "20",
        "owns" : ["car","PC","smartwatch","boat"],
    },

]

for person in persons:
    print("person name is :", person["name"], "salary is:", person["salary"], "age is:", person["age"],"owns :", person["owns"])



    ######## task2 part 2 #####

lst = [num for num in range(50) if  num % 2 == 0]
sum_even = sum(lst)
print(lst)
print("Sum of even numbers:", sum_even)

 ################ task2 part 2 #####
lst = [num for num in range(50) if  num % 2 != 0]
mult_odd = 1  # Initialize the product to 1
for num in lst:
    mult_odd *= num
print(lst)
print(" Multiple of odd numbers:", mult_odd)

####### task2 part3 ######
# lst = [num for num in range(50) if num >  ]
largest_num = (max(range(50)))
print ("The lagest number is : ",largest_num)
