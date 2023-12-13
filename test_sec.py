import pytest

from test_demo.Baseclass import Baseclass


class Testexample(Baseclass):
    def testnew(self,datause):
        log = self.test_log()
        log.info(datause[0])
        print(datause[1])
@pytest.mark.skip
def testha(Parak):
    print(Parak[1])
