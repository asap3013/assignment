from bs4 import BeautifulSoup
import requests
import mysql.connector


instagram_url = "https://www.instagram.com/hindavi_satkar_patil/"
response = requests.get(instagram_url)
htmlcontent = response.content
soup = BeautifulSoup(htmlcontent, 'html.parser')
for i in soup.find_all('title'):
    print(i.text)


# soup = BeautifulSoup(response.text)
# for x in soup.findAll('div', {'class':'_aacl _aacp _aacu _aacx _aad6 _aade'}):
#     print ("followers:-",(x))

# soup = BeautifulSoup(response.text)
# for x in soup.findAll('div', {'class':'_aacl _aacp _aacu _aacx _aad6 _aade'}):
#     print ("following",x)



# html = requests.get('https://www.instagram.com/hindavi_satkar_patil/')
# soup = BeautifulSoup(html.text, 'lxml')
# item = soup.select_one("meta[property='og:description']")
# name = item.find_previous_sibling().get("content").split("•")[0]
# followers = item.get("content").split(",")[0]
# following = item.get("content").split(",")[1].strip()
# print(f'{name}\n{followers}\n{following}')


