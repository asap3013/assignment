from bs4 import BeautifulSoup
import requests
import mysql.connector

instagram_url = "https://www.instagram.com/python_neosoft3/"

response = requests.get(instagram_url)
htmlcontent = response.content
soup = BeautifulSoup(htmlcontent, 'html.parser')
row = soup.find('link')
print(row.get("href"))


# conn = mysql.connector.connect(host="localhost", user="root",
#                                      password='p@ssw0rd',database='instadata')
# cursor = conn.cursor()
# cursor.execute(
#         "INSERT INTO insta_links (all_links) VALUES ('{}')".format(row.get('href')))
        
# conn.commit()
# cursor.close()
