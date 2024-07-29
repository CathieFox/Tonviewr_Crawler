import requests
import lxml
from bs4 import BeautifulSoup
import codecs


url = 'https://tonviewer.com/EQCOkbUDgcNt1CrM21H1y12WhIVotJJPgHmxpa5-EPQ-2n6g'

headers = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36"


response = requests.get(url)
#content = response.text

print(response.ok)


soup = BeautifulSoup(response.text, "lxml")


print(response.text)


#print(content)