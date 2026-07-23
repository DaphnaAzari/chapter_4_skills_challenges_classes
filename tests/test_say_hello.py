from lib.say_hello import say_hello
def test_says_name():
    result = say_hello("Daphna")
    assert result == "hello Daphna"