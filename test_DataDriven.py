import pytest

def get_data():
    return [
        ["amotoorione@gmail.com", "second"],
        ["amotooritwo@gmail.com", "second"],
        ["amotoorithree@gmail.com", "second"]
    ]


@pytest.mark.parametrize("username,password",get_data())
def test_login(username,password):
    print("Logged in using username: "+username+" and password" +password)



