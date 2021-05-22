# Course 5
# Python Project for Data Science
# 3- Extracting Stock Data Using a Web Scraping

''''
Extracting Stock Data Using a Web Scraping
Not all stock data is available via API in this assignment; you will use web-scraping to obtain financial data. You will be quizzed on your results.
Using beautiful soup we will extract historical share data from a web-page.
'''
#!pip install pandas
#!pip install requests
!pip install bs4
#!pip install plotly

import pandas as pd
import requests
from bs4 import BeautifulSoup

''''
Using Webscraping to Extract Stock Data
Use the requests library to download the webpage https://finance.yahoo.com/quote/AMZN/history?period1=1451606400&period2=1612137600&interval=1mo&filter=history&frequency=1mo&includeAdjustedClose=true. Save the text of the response as a variable named html_data.
'''
html_data= requests.get('https://finance.yahoo.com/quote/AMZN/history?period1=1451606400&period2=1612137600&interval=1mo&filter=history&frequency=1mo&includeAdjustedClose=true')

#Parse the html data using beautiful_soup.
soup = BeautifulSoup(html_data.text)

#Question 1 what is the content of the title attribute:
soup.title

''''
Using beautiful soup extract the table with historical share prices and store it into a dataframe named amazon_data. The dataframe should have columns Date, Open, High, Low, Close, Adj Close, and Volume. Fill in each variable with the correct data from the list col.

Hint: Print the col list to see what data to use
'''
amazon_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])

for row in soup.find("tbody").find_all("tr"):
    col = row.find_all("td")
    date =col[0].text
    Open =col[1].text
    high =col[2].text
    low =col[3].text
    close =col[4].text
    adj_close =col[5].text
    volume =col[6].text
    
    amazon_data = amazon_data.append({"Date":date, "Open":Open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True)

#Print out the first five rows of the amazon_data dataframe you created.
amazon_data.head()

