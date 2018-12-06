import os

from . import pytest, Vajehyab, client, bare_client, Responseobj, ERROR_CODES


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
    with pytest.raises(ValueError) as excep:
        vj = client.search_word(word="")
    assert "message should be provided" in str(excep.value)


def test_add_token(bare_client):
    assert bare_client.token == None
    bare_client.add_token(token_str="123")
    assert bare_client.token == "123"


def test_parse_response(client):
    success_str = "this is the actual text"
    resp = Responseobj(200, success_str)
    assert client.parse_response(resp) == success_str
    error_codes = [400, 401, 403, 404, 405, 500, 503]
    for err in error_codes:
        resp = Responseobj(err)
        assert client.parse_response(resp) == ERROR_CODES[str(err)]
