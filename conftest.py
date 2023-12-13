import pytest


@pytest.fixture(scope="class")
def setup():
    print("IN")
    yield
    print("OUT")

@pytest.fixture()
def datause():
    print("value is")
    return ["Megha","Abhi"]

@pytest.fixture(params=[("Chrome","Ani","B"),("Firefox","Cat"),("IE","dog")])
def Parak(request):
    return request.param