from bank import value

def test_здраствуйте():
    assert value("здравствуйте, Боб!") == 0

def test_здрасти():
    assert value("здрасти, Боб!") == 20

def test_hello():
    assert value("Hello, Harry!) == 100
