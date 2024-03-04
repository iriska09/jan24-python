# cities = ['New York', 'Los Angeles', 'Chicago', 'Huston', 'Boston']
# print(cities)
# print(cities[0])
# print(cities[-1])
# print(cities[3:])
# num = int(input("Enter your number between 1-10: "))
#     print (f"{num} is not valid")
#    num = int(input("Enter your number between 1-10: "))
#    print (f"Your number is {num}")

###testing!!!!!!!!!!

txt = "The best things in life are free!"
if "hfsf" in txt:
  print("Yes, 'free' is present.")
else :
  print("we couldn't found ")

## i didn't understand this well 

b = "Hello, World!"
print(b[::-8])
3##333333333
a = "Hello, World!"
print(a.split(","))

#### task1 ##### sorting the numbers
numbers =  [ 10 ,34 ,4 ,45,78,3,189]
numbers.sort ()
print(numbers)

##### task2 ###  create a list and revers it in the new list 
numbers =  [ 10 ,34 ,4 ,45,78,3,189]
numbers.sort ( reverse = True)
print(numbers)


###### task3 ######## create two list and 
#retern to new list containing the all elements between two list 
list1 = ["apple","banana","cherry","watermelon"]
list2 =  [ 10 ,34 ,4 ,45,78,3,189]
list3 = list1 + list2
print(list3)

### task4 ###### create a list of numbers and just print even numbers


list2 =  [ 10 ,34 ,4 ,45,78,3,189]
evennumbers = [num for num in list2 if num  % 2 != 0] 
print(evennumbers)

## just trying

for i in range(1,4):
    for x in range(1,4):
        for j in range(1,4):
                print(i,x,j)
