"""
Check if the user can log in based on correct username and password.

I/p

username = "admin"
password = "1234"

O/p
✅ Login Successful


For the Fail condition Other O/P = ❌ Invalid Credentials
"""

username = "admin"
password = "1234"

user_username = input("Enter username: ").strip()
user_password = input("Enter password: ").strip()

if user_username == username and user_password == password:
    print("Login Successful")
else :
    print("Invalid credentials")