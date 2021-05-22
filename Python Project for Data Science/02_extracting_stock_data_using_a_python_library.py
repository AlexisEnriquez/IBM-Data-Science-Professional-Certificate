# Course 5
# Python Project for Data Science
# 2- Extracting Stock Data Using a Python Library

''''
Extracting Stock Data Using a Python Library
A company's stock share is a piece of the company more precisely:

A stock (also known as equity) is a security that represents the ownership of a fraction of a corporation. This entitles the owner of the stock to a proportion of the corporation's assets and profits equal to how much stock they own. Units of stock are called "shares." [1]

An investor can buy a stock and sell it later. If the stock price increases, the investor profits, If it decreases,the investor with incur a loss.  Determining the stock price is complex; it depends on the number of outstanding shares, the size of the company's future profits, and much more. People trade stocks throughout the day the stock ticker is a report of the price of a certain stock, updated continuously throughout the trading session by the various stock market exchanges.

You are a data scientist working for a hedge fund; it's your job to determine any suspicious stock activity. In this lab you will extract stock data using a Python library. We will use the yfinance library, it allows us to extract data for stocks returning data in a pandas dataframe. You will use the lab to extract.
'''
!pip install yfinance
#!pip install pandas

import yfinance as yf
import pandas as pd

''''
Using the yfinance Library to Extract Stock Data
Using the Ticker module we can create an object that will allow us to access functions to extract data. To do this we need to provide the ticker symbol for the stock, here the company is Apple and the ticker symbol is AAPL.
'''
apple = yf.Ticker("AAPL")

''''
Now we can access functions and variables to extract the type of data we need. You can view them and what they represent here https://aroussi.com/post/python-yahoo-finance.

Stock Info
Using the attribute info we can extract information about the stock as a Python dictionary.
'''
apple_info=apple.info
apple_info

#We can get the 'country' using the key country
apple_info['country']

#Extracting Share Price
#A share is the single smallest part of a company's stock that you can buy, the prices of these shares fluctuate over time. Using the history() method we can get the share price of the stock over a certain period of time. Using the period parameter we can set how far back from the present to get data. The options for period are 1 day (1d), 5d, 1 month (1mo) , 3mo, 6mo, 1 year (1y), 2y, 5y, 10y, ytd, and max.
apple_share_price_data = apple.history(period="max")

#The format that the data is returned in is a Pandas DataFrame. With the Date as the index the share Open, High, Low, Close, Volume, and Stock Splits are given for each day.
apple_share_price_data.head()

#We can reset the index of the DataFrame with the reset_index function. We also set the inplace paramter to True so the change takes place to the DataFrame itself.
apple_share_price_data.reset_index(inplace=True)

#We can plot the Open price against the Date:
apple_share_price_data.plot(x="Date", y="Open")

##Extracting Dividends
#Dividends are the distribution of a companys profits to shareholders. In this case they are defined as an amount of money returned per share an investor owns. Using the variable dividends we can get a dataframe of the data. The period of the data is given by the period defined in the 'history` function.
apple.dividends

#We can plot the dividends overtime:
apple.dividends.plot()

##Exercise
#Now using the Ticker module create an object for AMD (Advanced Micro Devices) with the ticker symbol is AMD called; name the object amd.
amd = yf.Ticker("AMD")

#Question 1 Use the key 'country' to find the country the stock belongs to, remember it as it will be a quiz question.
amd_info=amd.info
amd_info
amd_info['country']

#Question 2 Use the key 'sector' to find the sector the stock belongs to, remember it as it will be a quiz question.
amd_info['sector']

#Question 3 Find the max of the Volume column of AMD using the history function, set the period to max.
amd_volume = amd.history(period="max")
print(amd_volume)

