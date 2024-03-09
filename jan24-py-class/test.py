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
mytuples = ("cherry", "apple", "banana", "banana", ["21312","8694397","314-241"])
print (mytuples.count("banana"))
for elem in mytuples:
    print (elem)
####### here we can change we have list in the tuples 
person = ("Yrys", "Bolotbek", "08.05.02", "123-456", ["21312423","8694397","314-241"])
person[-1][0] = "989-99"
print (person)
########## tuples we can not change but if we have a string inside of the tuples we 
we can change the string 
lst = ["21312423", ("Yrys", "Bolotbek", "08.05.02", "123-456", )]
(lst[0]) = "5448-35"
print(lst)
person = {
"name" : ("Yrys",), 
"lastname": "Bolotbek", 
"dob": "08.05.02",
"number": ["123-456","4526-5375"]
}
# person["name"] [0]
person["name"] = "Khusrav"

# print(person)
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

task 4

connections = [
    ('Amsterdam', 'Dublin', 100),
    ('Amsterdam', 'Rome', 140),
    ('Rome', 'Warsaw', 130),
    ('Minsk', 'Prague', 95),
    ('Stockholm', 'Rome', 190),
    ('Copenhagen', 'Paris', 120),
    ('Madrid', 'Rome', 135),
    ('Lisbon', 'Rome', 170),
    ('Dublin', 'Rome', 170),
    ]
rome_how_many = [elem for elem in connections if elem[1] == 'Rome']
print (len(rome_how_many))
time_finding = sum(elem[2] for elem in rome_how_many) / len(rome_how_many)
print (time_finding)
print(f"{len(rome_how_many)} here is the time {time_finding} minutes")




