"""
In automation, you often compare expected and actual outputs.
Write code to check if a test case passed or failed.

expected_title = "Dashboard"
actual_title = "Dashboard "

✅ Test Passed – Title matches

True - why >  Strip and convert them into the lowercase = both of them are equal.
"""

expected_title = (input("Enter the expected title: ").strip())
expected_title = expected_title.lower()
actual_title = (input("Enter the actual title: ").strip())
actual_title = actual_title.lower()

if actual_title == expected_title:
    print("Testcase is Passed")
else:
    print("Testcase is Failed")


