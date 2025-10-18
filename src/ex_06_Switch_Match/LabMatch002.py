print("Enter which test you want to run")
test_type = input("Enter the test type : API, UI, Performance, Security\n")

match test_type:
    case "API":
        print("We are running a postman API Testcase")
    case "UI":
        print("We are running a Selenium Testcase")
    case "Performance":
        print("We are running a Performance Test")
    case "Security":
        print("We are running a Security Testcase")
    case _:
        print("Invalid input")