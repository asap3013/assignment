import tweepy as tw
import mysql.connector
from fpdf import FPDF
import PyPDF2
import pandas as pd
import pdfkit

consumer_key = "GLIgsx9Kl5T7B2xifygeIXdGY"
consumer_secret = "JJOgeW0rMv4PVOeyk4BYvJkEYeebLbRUPa1H35o7SZCRDUWpUs"
access_token = "1554767943707561984-lLDSOwa2xiJxHRVjbDa4Uw6TBIYOjI"
access_token_secret = "vJGMLZBzp13CBLEna5f6xO99EepBpI67zR1NP4CZq3XD7"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAO82fgEAAAAAFGPDTfEG2kUP8MMeXkZ4%2B4D05ck%3DWiDmANLrKsteqmSokpFrfxbuIcKCjP0exUFsIBekC4UOoCt5UT"


auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)


api = tw.API(auth)
public_tweets = api.home_timeline()
twitter_data = []
for tweet in public_tweets:
    print((tweet.text),end = '')
    twitter_data.append(tweet.text)

# print(twitter_data)

pdf = FPDF() 
pdf.add_page() 
pdf.add_font('Calibri Regular', '', '/home/neosoft/Desktop/Calibri/Calibri.ttf')
pdf.set_font('Calibri Regular', '', 12)
for x in twitter_data:
    pdf.cell(200, 10,x)
    # pdf.set_left_margin(32)
    pdf.set_right_margin(5)
    pdf.write(8,x)

pdf.output("/home/neosoft/Desktop/python_assignment/tweet_data2.pdf") 



conn = mysql.connector.connect(host="localhost", user="root",
                                     password='p@ssw0rd',database='twitter_data')
cursor = conn.cursor()

insert_tweet = 'INSERT INTO twits_scrapped (Tweets) VALUES ("{}")'.format(x)
cursor.execute(insert_tweet)
        
conn.commit()
cursor.close()
print('Done')


