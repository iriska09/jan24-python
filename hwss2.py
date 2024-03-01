#your password requires 
#at least 1 letter between [a-z]
#at least 1 number between [0-9]
#at least 1 upercase letter [A-Z]
#minimum length of the password 8 letters 
#maximum length of the password 23 letters 
username = input(" Please enter the username or email: ")
password = input(" Please enter your password :")


if len(password) > 23 or len(password) < 8:
    print("Maximum length of transaction password: 23 and minimum is 8")
else:
    print("Valid password! Good job")

if  (password.isalnum() or password.upper() == password or password.lower() == password):
    print("Password must have at least 1 uppercase letter, 1 lowercase letter, 1 number, 1 special character")
else:
    print("strong password")
