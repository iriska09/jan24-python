#octal oct() octal number is from 0-7 only we can use 
print(oct(43))
#output 0o53

#hexadecimal from 0-9 and from a to f only we can use #### hex()
print(hex(30))
#output is 0x1e
#and the binary numbers starts with ##### 0b ######


jan24_names = ["Aiperi","Khusrav","Fatima","Yrys","Myroslav","Dastan","Tatina"]
for word in jan24_names:
    print("Hello" , word )

#####while loop 
    inp = input("Please provide your input: ")
    while len(inp) ==0:
        inp = input("Please enter your inout(Noinput provided): ")
    print(inp)
    break
############## tuples 
jan24_names = (
    "Aiperi",
    "Fatima",
    "Yrys",
    "Dastan",
)
print(jan24_names)

person = "John", "Doe", "233423", "4342-423", ["3224-234","2341-256","986798-675"]
print(type(person))
for info in person:
    print(info)

##### here we have list in tuples and we can change the list in duples  

person = "John", "Doe", "233423", "4342-423", ["3224-234","2341-256","986798-675"]
person[-1][0] = "334719354"
print(person)
########tuples that we can not change 

person = {
"name": ("John"),
"lastname" : "Doe",
"number" : "233423",
"ssn" :"4342-423",
 "phone" : ["3224-234","2341-256","986798-675"]
 }
person["name"][0] = "Johnson"
print(person)

########### information with tuples 



movies = [
    {
        "name" : "Descendants",
        "year" : "2016",               #all is dictionary
        "director" : "Lee Eung-bok",
    },
    {
        "name" : "upgraded",
        "year" : "04.20.2016",
        "director" : "john",
        "main actors" : ["arche" "marca"],
    }
]

for movie in movies:  #iterating inside of a list ---> dictionary
    # print("-------------")
    # for info in movie.():
    print("Movie title is:", movie["title"], "Year is", movie["year"])
       

set can hold multy values but we dont have accsess ###### sets holds only uniqe values 

lst = [1,1,1,1,2,2,2,3,3,3,3,"Hello", "Hello", "World"]
st = set(lst)
lst = list(st)
print(lst[-1])


################# sequance deletes multiples duplicates and gives only uniqe numbers 
st = {4,5,6,7,8,8,9,9,19}
for num in st:
    print(num)
Do not give true and false in the sets 
######### sets using
set_a = {1,2,3,4,5}
set_b = {4,5,6,8,9}
union_set = set_a | set_b  ##### also we can use & to have same values
print(union_set)

### comprehensions 
#colection data types :
d = {i : i ** 2 for i in range(1, 5)}
print(d)