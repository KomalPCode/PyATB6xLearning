def before_after_ui_test(func):

    def wrapper():
        print("Before running UI test")
        func()
        print("After running UI test")

    return wrapper


@before_after_ui_test
def test_ui():
    print("I am testing UI")

test_ui()