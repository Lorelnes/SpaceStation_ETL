from urllib.error import HTTPError, URLError
from constants import url
from urllib import request
import json
import logging

logging.basicConfig(level=logging.INFO)

def extract_data(url: str) -> dict:
    try:
        response = request.urlopen(url)
        data = json.dumps(response.read().decode())
        response.close()
        return json.loads(data)
    except HTTPError as e:
        logging.error(f'HTTPError occured: {e}')
    except URLError as e:
        logging.error(f'URLError occured: {e}')
    except TimeoutError as e:
        logging.error(f'TimeoutError occured: {e}')
    except Exception as e:
        logging.error(f'An unexpected error occured: {e}')

    return data




