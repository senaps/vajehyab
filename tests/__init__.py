import pytest

from vajehyab import Vajehyab
from vajehyab.utils.default_vals import ERROR_CODES


@pytest.fixture
def client():
    vl = Vajehyab(token="test-token")
    yield vl


@pytest.fixture
def bare_client():
    vl = Vajehyab()
    yield vl


class Responseobj:
    def __init__(self, status_code, text=None):
        self.status_code = status_code
        self.txt = text