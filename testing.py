import pytest

@pytest.mark.parametrize("username, password", [("admin", "admin"), ("admin", "Ram")])
def test_admin(username, password):
    assert username == password

