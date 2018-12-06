import logging

import requests

from .utils.default_vals import TYPES, PER_PAGE_MAX, DBS

logger = logging.getLogger(__name__)

class Vajehyab:
    """Vajehyab python interface


    """
    def __init__(self, token=None, url="http://api.vajehyab.com/v3/"):
        self.token = token
        self.url = url
        self.params = None

    def add_token(self, token_str):
        self.token = str(token_str)

    def search_word(self, word=None, search_type='exact', page=None,
                    per_page=None,
                    dbs=None):
        """search a word

        this function will send a request to vajehyab for it's search query
        this method supports multiple `search_type`s for searching. valid
        types are :
            `exact`: for exact word match
            `ava` : for same words based on their sound
            `like`: for same words based on their spelling
            `text`: for search based on the meaning
        method also supports `page` entry which will specify the page in the
        pagination system. alongside the `per_page` which specifies how many
        results should be shown.
        `per_page` should be maxed to `50` and has a default value of `10`.
        using the `dbs`, method specifies what databases should be searched for
        the word.

        :param word: word or the sentence one is going to query
        :param search_type: type of the search
        :param page: number of page of results pages that should be retrived
        :param per_page: number of rows per page that should be shown
        :param dbs: db names to search from
        :return: a list of words that match searched word in the db.
        """
        self.params = dict()
        if not word:
            message = f"message should be provided"
            logger.error(message)
            raise ValueError(message)
        if search_type.lower() not in TYPES:
            message = f"`{search_type}` is not supported"
            logger.error(message)
            raise ValueError(message)
        if page and (not isinstance(page, int)):
            message = f"page should be an int variable, {type(page)} provided"
        if per_page and per_page > PER_PAGE_MAX:
            message = f"per_page should be maxed to {PER_PAGE_MAX}, {per_page}" \
                      f"used, which is bigger."
            logger.error(message)
            raise ValueError(message)
        if dbs and dbs.lower() not in DBS:
            message = f"db name of {dbs} is not recognized."
            logger.error(message)
            raise ValueError(message)
        self.params["q"] = word
        self.params["type"] = search_type
        if page:
            self.params["start"] = page
        if per_page:
            self.params["rows"] = per_page
        if dbs:
            self.params["filter"] = dbs
        result = self.make_request()
        return result

    def make_request(self):
        return self.parse_response(resp=requests.get(url=self.url,
                                                     params=self.params))

    def parse_response(self, resp):
        responses = {
            "200": resp.txt,
            "400": "failed to parse parameters",
            "401": "invalid token has been used",
            "403": "this token is banned from vajehyab",
            "404": "word is not found in vajehyab databases",
            "405": "unknown HTTP method used to send data",
            "500": "server has failed to respond",
            "503": "server is down",
            }
        return responses[str(resp.status_code)]


