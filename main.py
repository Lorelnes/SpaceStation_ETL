from extraction import extract_data
from constants import url

all_data = []
for i in range(10):
    data = extract_data(url)
    all_data.append(data)
    print(data)