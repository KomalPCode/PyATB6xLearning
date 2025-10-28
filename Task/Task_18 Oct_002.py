"""
Question 2 :

An API sometimes fails due to network delays.

Write a program to retry the API call 3 times until the response code becomes 200.

If it still fails after 3 tries, print a failure message.

Hint: Use a while loop with a counter.
Hint: Use a while loop with a counter.

Expected Output Example:

Attempt 1: Response 500

Attempt 2: Response 200

✅ Test Passed
"""

retries = 1
while (retries<=3):
    response_code = int(input("Enter the Response code : ").strip())
    if response_code == 200:
        print("Test Passed")
        break
    retries = retries + 1
    if retries > 3:
        print("Test Failed")
