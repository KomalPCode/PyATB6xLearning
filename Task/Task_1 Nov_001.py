"""
Write a Function to Check Test Case Status

Problem:

Write a function check_status(status_code) that returns:

"PASS" if status_code = 200

"FAIL" if status_code = 400 or 500

"UNKNOWN" otherwise

Example Input & Output:

print(check_status(200))   # PASS

print(check_status(500))   # FAIL

print(check_status(302))   # UNKNOWN
"""
def check_status(status_code):

    match status_code:
        case 200:
            print("Request is PASS")
        case 400 | 500:
            print("Request is FAIL")
        case _:
            print("Request is UNKNOWN")


code_of_status = int((input("Enter status code : ")))
check_status(code_of_status)