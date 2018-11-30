import logging

import requests

from .utils.default_vals import TYPES, PER_PAGE_MAX, DBS

logger = logging.getLogger(__name__)

class Vajehyab:
    """Vajehyab python interface


    """
    def __init__(self, token=None, base_url="http://api.vajehyab.com/v3/"):
        self.token = token
        self.base_url = base_url

    def make_url(self, params, method):
        """

        :param kwargs:
        :return:
        """
        if not self.token:
            message = "token is not set, please set token using self.add_token"
            logger.error(message)
            raise ValueError(message)
        token_str = f"{method}?token={self.token}"
        return self.base_url + token_str +params

    def add_token(self, token_str):
        self.token = token_str

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
        param_string = f"&q={word}&type={search_type}"
        if page:
            param_string += f"&start={page}"
        if per_page:
            param_string += f"&rows={per_page}"
        if dbs:
            param_string += f"&filter={dbs}"
        result = self.call_query(method="search", param_string=param_string)
        return result

    def call_query(self, method, param_string):
        url = self.make_url(params=param_string, method=method)
        return self.make_request(url)

    def make_request(self, url):
        return self.parse_response(resp=requests.get(url))

    def parse_response(self, resp):
        if resp.status_code == 200:
            # successfull query
            return resp.text
        elif resp.status_code == 400:
            # failed to parse parameters
            pass
        elif resp.status_code == 401:
            #token is not valid
            pass
        elif resp.status_code == 403:
            # this token is banned to use the site
            pass
        elif resp.status_code == 404:
            # word is not found
            print("this word doesn't look like anything to me:)")
        elif resp.status_code == 405:
            # unknown method
            pass
        elif resp.status_code == 500:
            # failed server
            pass
        elif resp.status_code == 503:
            # server is down
            pass
        else:
            # this is new then do something with it!:)
            pass


