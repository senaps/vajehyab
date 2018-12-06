TYPES = ['exact', 'ava', 'like', 'text']

PER_PAGE_MAX = 50

DBS = ['dehkhoda', 'moein', 'amid', 'motaradef', 'farhangestan',
       'sareh', 'ganjvajeh', 'wiki', 'slang', 'quran', 'name',
       'thesis', 'isfahani', 'bakhtiari', 'tehrani', 'dezfuli',
       'gonabadi', 'mazani']

ERROR_CODES = {
            "400": "failed to parse parameters",
            "401": "invalid token has been used",
            "403": "this token is banned from vajehyab",
            "404": "word is not found in vajehyab databases",
            "405": "unknown HTTP method used to send data",
            "500": "server has failed to respond",
            "503": "server is down",
            }