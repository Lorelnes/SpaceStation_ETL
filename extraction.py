from constants import url
from urllib import request
import json

def extract_data(url):
    response = request.urlopen(url)
    data = json.loads(response.read().decode())
    return data




