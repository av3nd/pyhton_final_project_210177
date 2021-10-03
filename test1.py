import pytest

@pytest.mark.parametrize("username, password", [("admin", "admin"), ("admin", "Ram")])
def test_admin(username, password):
    assert username == password

@pytest.fixture()
def tester():
    FirstName = "Avend"
    LastName = "Tabdar"
    Id = 10234
    Address = "Kanchanbari"
    City = "Biratnagar"
    State = "Morang"
    Zipcode = 42044

    return [FirstName, LastName,Id,Address,City,State,Zipcode]

def testing_1(tester):
    FirstName = "Avend"
    assert tester[0] == FirstName

def testing_2(tester):
    LastName = "Tabdar"
    assert tester[1] == LastName

def testing_2(tester):
    LastName = "Tabdar"
    assert tester[1] == LastName

def testing_3(tester):
    Id = 10234
    assert tester[2] == Id

def testing_4(tester):
    Address = "Kanchanbari"
    assert tester[3] == Address

def testing_5(tester):
    City = "Biratnagar"
    assert tester[4] == City

def testing_6(tester):
    State = "Morang"
    assert tester[5] == State

def testing_7(tester):
    Zipcode = 42044
    assert tester[6] == Zipcode

def testing_8(tester):
    FirstName = "Ram"
    assert tester == FirstName

def testing_9(tester):
    LastName = "Dhakal"
    assert tester == LastName

def testing_10(tester):
    City = 1234
    assert tester == City

