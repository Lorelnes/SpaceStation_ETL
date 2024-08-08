from extraction import extract_data
from constants import url
import time

while True:
    data = extract_data(url)
    print(data)
    time.sleep(60)