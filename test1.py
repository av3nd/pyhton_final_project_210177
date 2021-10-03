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
