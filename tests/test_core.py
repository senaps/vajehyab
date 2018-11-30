import os

from .client import *

def test_makeinstance():
    vj = Vajehyab()
    assert isinstance(vj, Vajehyab)
    assert vj.token == None
    vj = Vajehyab(token="test")
    assert isinstance(vj, Vajehyab)
    assert vj.token == "test"


def test_searchword_word(client):
    with pytest.raises(ValueError) as excep:
        client.search_word()
    assert str(excep.value) == 'message should be provided'


def test_searchword_type(client):
    with pytest.raises(ValueError) as excep:
        client.search_word(word="test", search_type="wrong")
    assert str(excep.value) == '`wrong` is not supported'


def test_searchword_perpage(client):
    with pytest.raises(ValueError) as excep:
        client.search_word(word="test", per_page=60)
    assert 'per_page should be maxed to' in str(excep.value)

def test_search_word(client):
    vj = client.search_word(word="")