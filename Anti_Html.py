import  requests
from bs4 import BeautifulSoup
obj = requests.get("http://www.google.com")
soup = BeautifulSoup(obj.content,'html.parser').text
print(soup)