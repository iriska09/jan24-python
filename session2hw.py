print ("please provide your password : your password must be 8 char long,must contain one upercase letter,lowercase letter,at least one digit,one special character ")
passwd = input  ("Please enter your password : ")
#we are checking the password should have at least
# if len(passwd) < 8:
#     print("Password must be at least 8 characters long.")
#     elif 
while True: # we are using wile  true loop to repeatedly check the password until it meets the specified criteria.
    # Checking if the password is 8 characters long.
    if len(passwd) < 8:
        print("Password must be at least 8 characters long.")
    # we are checking  if the password contains at least one uppercase letter.
    elif not any(let.isupper() for let in passwd):
        print("Password must contain at least one uppercase letter.")
    # here we are check if the password contains at least one lowercase letter.
    elif not any(let.islower() for let in passwd):
        print("Password must contain at least one lowercase letter.")
    # Check if the password contains at least one number.
    elif not any(let.isdigit() for let in passwd):
        print("Password must contain at least one number.")
    # If all criteria are met, print a success message and break out of the loop.
    elif not any(let in "!@#$%^&*()_-+=" for let in passwd):
        print("Password must contain at least one special character.")
    else:
        print("Password is valid.")
        break

    # If the password is not valid, prompt the user to enter another password.
    passwd = input()
