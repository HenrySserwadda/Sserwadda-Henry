users ={"Mukasa":"password1", "Jovan":"password2", "Sserwadda":"password3", "Angel":"password4"}
username = input("Enter your username: ")
password = input("Enter your password: ")
if username in users:
    if password == users[username]:
        print("Login successful!")
    else:
        print("Incorrect password.")
else:
    print("Username not found.") 