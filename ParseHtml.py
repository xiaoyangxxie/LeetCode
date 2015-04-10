__author__ = 'xyang'
import urllib
from bs4 import BeautifulSoup
content = urllib.urlopen('http://10.197.55.159:8080/DomainEditor?ADC_TOKEN=GUSB-30N3-M4FH-4DF4-EN4J-WH72-9PPY-AIIV&command=chooseSite&domainCode=0ac5379f-02-14c9763b992-bb021811-c6f#0ac5379f-35-14c97660b86-15a36279-c6f').read()
soup = BeautifulSoup(content)
#head = soup.find_all('a')
for link in soup.find_all('a'):
    print link