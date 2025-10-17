#You receive an API response code from your test script.
#Write an if-else block to check whether the response is successful (status code 200) or not.

#I/P response = 404 , O/P ❌ Failed API Request
#I/P response = 200 , O/P ✅ Passed API Request

response = int(input("Enter the status code: ").strip())

if response == 200 :
    print("Passed API request")
else:
    print("Failed API request")