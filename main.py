from extraction import Extraction
from constants import url
import time

while True:
    extractor = Extraction(url)
    data = extractor.extract_data()
    print(data)
    time.sleep(60)