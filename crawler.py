#site - https://urlhaus.abuse.ch/browse/
import os
import re
import time
import hashlib
import requests
from tqdm import tqdm
from random import randint
from bs4 import BeautifulSoup as bs

for x in range(2, 70000, 1):
    url = "https://urlhaus.abuse.ch/browse/page/%s/" % x
    print(url)
    response = requests.get(url)
    #print(response.text)
    soup = bs(response.text, 'html.parser')
    table = soup.find('table', {'class': 'table'})
    download_link = []

    for row in table.findAll('a'):
        malware = re.findall('^http.*exe$', str(row.get_text()))
        if malware :
            download_link = malware

    print(download_link)

    # downlaod malware
    for malware in download_link :
        res = requests.get(malware, stream=True)

        with open("../win_virus/malware", "wb") as handle:
            for data in tqdm(res.iter_content()):
                handle.write(data)

        with open("../win_virus/malware","rb") as f:
            bytes = f.read() # read entire file as bytes
            readable_hash = hashlib.sha256(bytes).hexdigest()
            new_name = "../win_virus/%s" % readable_hash
            os.rename("../win_virus/malware", new_name)

    # go to next page
    time.sleep(randint(12,17))
