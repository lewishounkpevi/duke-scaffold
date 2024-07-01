from hello import add, subtract


# def setup_function(function):
#     print(f" Running Setup: {function.__name__}")
#     function.x = 10


# def teardown_function(function):
#     print(f" Running Teardown: {function.__name__}")
#     del function.x


### Run to see failed test
def test_hello_add():
    assert add(10) == 11

def test_hello_subtract():
    assert subtract(10) == 9