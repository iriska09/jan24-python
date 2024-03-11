# #####task1

# def my_lists(list1, list2):
#     new_list = [elem for elem in list1 if elem not in list2]
#     new_list.sort()
#     return new_list


# list1 = ["1","2","3","banana","apple","cherry"]
# list2 = ["1","2","apple"]
# print(my_lists(list1,list2))

# ##task2 
# print("Welcome to the calculator program!")
# num1 = int(input("Enter your first number to count: "))
# num2 = int(input("Enter your second number to count: "))
# char= input("Enter any of these characters to do your operation +,-,*,/: ")
# for char in char:
#     if char == "+":
#         result = num1 + num2 
#     elif char == "-":
#         result = num1 - num2
#     elif char == "*":
#         result = num1 * num2
#     elif char == "/":
#         # result = num1 / num2
#         try:
#             result = num1 / num2
#         except ZeroDivisionError:
#             print("Cannot divide by zero!")
#             break
#         # finally:
#         #     print(result)
#         #     break
#     else:
#         result = num1 / num2
#         print("Enter correct character to count")
#         break  # Exit the loop if an invalid operation is encountered

#     print(f"The result of the operation is:", result)






# #     ###task 3 
#     # x = int(input("Enter your number: "))
# def num_average(lst):
#     num_av = sum(lst) / len(lst)
#     return num_av

# lst = [34,5,6,7,13]
# # print(f"{len(lst)} average of the num" , num_average)
# print(num_average(lst))





def addition(num1,num2):
    return num1 + num2
def multipication(num1,num2):
    return num1 * num2
def subtraction(num1,num2):
    return num1 - num2
def devision(num1,num2):
    # if num2 == 0:

    #     return ("division by 0 is invalid!")
    # else:
        return num1 / num2
   
def calculator():
    inp1 = int(input("First number"))
    inp2 = int(input("Second number"))
    inp3 = input(("Enter any of these characters to do your operation +,-,*,/: "))
    
    if "+" in inp3:
        result = inp1 + inp2
        print(result)
    elif "-" in inp3:
        result = inp1 - inp2
        print(result)
    elif "*" in inp3:
        result = inp1 * inp2
        print(result)
    elif "/" in inp3:
        try:
            result = inp1 / inp2
        except ZeroDivisionError:
            print("Cannot divide by zero!")
            return
        else:
        
        #  = num1 / num2
        # print("Enter correct character to count")
        # break  # Exit the loop if an invalid operation is encountered

            print(f"The result of the operation is:, {result}")
calculator()

   
 


