correct_username = "Hriddham"
correct_password = "Hriddham123"

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == correct_username and password == correct_password:
    print("Access Granted")
    print("Here is your reward: https://youtu.be/Aq5WXmQQooo?si=lAhWL4mbt4rUFP1S")

elif username == correct_username or password == correct_password:
    print("Invalid Password")

else:
    print("Invalid Username")

