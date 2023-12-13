import pytest


@pytest.mark.usefixtures("setup")
class Testall:

    def test1(self):
        print("monkey")

    def test2(self):
        print("donkey")

    def test3(self):
        print("pinkey")

    def test4(self):
        print("inkey")