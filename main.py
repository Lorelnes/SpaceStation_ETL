from extraction import Extraction
from constants import url
from loading import Directory
import time

while True:
    extractor = Extraction(url)
    data = extractor.extract_data()
    print(data)
    time.sleep(60)

parent_directory = "/home/user/PycharmProjects/SpaceStation_ETL"
directory = 'data_lake'
dir = Directory(parent_directory, directory)
dir.create_directory()