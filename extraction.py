from urllib.error import HTTPError, URLError
from constants import url
from urllib import request
import json
import logging

logging.basicConfig(level=logging.INFO)

class Extraction:
    def __init__(self, url: str):
        self.url = url

    def extract_data(self) -> dict:
        '''
        This function extracts data from the given URL.
        :param: url
        :returns: dictionary with the extracted data.
        '''
        try:
            response = request.urlopen(self.url)
            data = json.dumps(response.read().decode())
            response.close()
            return data
        except HTTPError as e:
            logging.error(f'HTTPError occured: {e}')
        except URLError as e:
            logging.error(f'URLError occured: {e}')
        except TimeoutError as e:
            logging.error(f'TimeoutError occured: {e}')
        except Exception as e:
            logging.error(f'An unexpected error occured: {e}')
            return None




