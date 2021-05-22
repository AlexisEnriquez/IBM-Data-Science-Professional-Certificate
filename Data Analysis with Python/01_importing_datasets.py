# Course 7
# Data Analysis with Python
# 1- Importing Datasets

''''
Objectives
After completing this lab you will be able to:

Acquire data in various ways
Obtain insights from Data with Pandas library
'''

''''
Data Acquisition
There are various formats for a dataset, .csv, .json, .xlsx etc. The dataset can be stored in different places, on your local machine or sometimes online.
In this section, you will learn how to load a dataset into our Jupyter Notebook.
In our case, the Automobile Dataset is an online source, and it is in CSV (comma separated value) format. Let's use this dataset as an example to practice data reading.

data source: https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data
data type: csv
The Pandas Library is a useful tool that enables us to read various datasets into a data frame; our Jupyter notebook platforms have a built-in Pandas Library so that all we need to do is import Pandas without installing.
'''
# import pandas library
import pandas as pd
import numpy as np

''''
Read Data
We use pandas.read_csv() function to read the csv file. In the bracket, we put the file path along with a quotation mark, so that pandas will read the file into a data frame from that address. The file path can be either an URL or your local file address.
Because the data does not include headers, we can add an argument headers = None inside the read_csv() method, so that pandas will not automatically set the first row as a header.
You can also assign the dataset to any variable you create.
'''
# Import pandas library
import pandas as pd

# Read the online file by the URL provides above, and assign it to variable "df"
other_path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"
df = pd.read_csv(other_path, header=None)

''''
After reading the dataset, we can use the dataframe.head(n) method to check the top n rows of the dataframe; where n is an integer. Contrary to dataframe.head(n), dataframe.tail(n) will show you the bottom n rows of the dataframe.
'''
# show the first 5 rows using dataframe.head() method
print("The first 5 rows of the dataframe") 
df.head(5)

#check the bottom 10 rows of data frame "df".
print("Bottom 10 rows of the dataframe\n")
df.tail(10)

''''
Add Headers
Take a look at our dataset; pandas automatically set the header by an integer from 0.

To better describe our data we can introduce a header, this information is available at: https://archive.ics.uci.edu/ml/datasets/Automobile

Thus, we have to add headers manually.

Firstly, we create a list "headers" that include all column names in order. Then, we use dataframe.columns = headers to replace the headers by the list we created.
'''
# create headers list
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
print("headers\n", headers)

#We replace headers and recheck our data frame
df.columns = headers
df.head(10)

#we need to replace the "?" symbol with NaN so the dropna() can remove the missing values
df1=df.replace('?',np.NaN)

#we can drop missing values along the column "price" as follows
df=df1.dropna(subset=["price"], axis=0)
df.head(20)

#Find the name of the columns of the dataframe
# Write your code below and press Shift+Enter to execute 
print(df.columns)

''''
Save Dataset
Correspondingly, Pandas enables us to save the dataset to csv by using the dataframe.to_csv() method, you can add the file path and name along with quotation marks in the brackets.

For example, if you would save the dataframe df as automobile.csv to your local machine, you may use the syntax below:
'''
df.to_csv("automobile.csv", index=False)

''''
Basic Insight of Dataset
After reading data into Pandas dataframe, it is time for us to explore the dataset.
There are several ways to obtain essential insights of the data to help us better understand our dataset.

Data Types
Data has a variety of types.
The main types stored in Pandas dataframes are object, float, int, bool and datetime64. In order to better learn about each attribute, it is always good for us to know the data type of each column. In Pandas:
'''
df.dtypes
# check the data type of data frame "df" by .dtypes
print(df.dtypes)
# if we would like to get a statistical summary of each column, such as count, column mean value, column standard deviation, etc. We use the describe method:
dataframe.describe()
# This method will provide various summary statistics, excluding NaN (Not a Number) values.
df.describe()

''''
This shows the statistical summary of all numeric-typed (int, float) columns.
For example, the attribute "symboling" has 205 counts, the mean value of this column is 0.83, the standard deviation is 1.25, the minimum value is -2, 25th percentile is 0, 50th percentile is 1, 75th percentile is 2, and the maximum value is 3.
However, what if we would also like to check all the columns including those that are of type object.

You can add an argument include = "all" inside the bracket. Let's try it again.
'''
# describe all the columns in "df" 
df.describe(include = "all")

''''
You can select the columns of a data frame by indicating the name of each column, for example, you can select the three columns as follows:

dataframe[[' column 1 ',column 2', 'column 3']]

Where "column" is the name of the column, you can apply the method ".describe()" to get the statistics of those columns as follows:

dataframe[[' column 1 ',column 2', 'column 3'] ].describe()

Apply the method to ".describe()" to the columns 'length' and 'compression-ratio'.
'''
# Write your code below and press Shift+Enter to execute 
df[['length', 'compression-ratio']].describe()

#Another method you can use to check your dataset is:
dataframe.info()

# look at the info of "df"
df.info()