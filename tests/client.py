import pytest

from vajehyab import Vajehyab

@pytest.fixture
def client():
    vl = Vajehyab(token="test-token")
    yield vl