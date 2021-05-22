# Course 6
# Dtabases and SQL for Data Science with Python
# 5- Analyzing a real world data-set with SQL and Python

''''
Objectives
After completing this lab you will be able to:

Understand a dataset of selected socioeconomic indicators in Chicago
Learn how to store data in an Db2 database on IBM Cloud instance
Solve example problems to practice your SQL skills
Selected Socioeconomic Indicators in Chicago
The city of Chicago released a dataset of socioeconomic data to the Chicago City Portal. This dataset contains a selection of six socioeconomic indicators of public health significance and a “hardship index,” for each Chicago community area, for the years 2008 – 2012.

Scores on the hardship index can range from 1 to 100, with a higher index number representing a greater level of hardship.

A detailed description of the dataset can be found on the city of Chicago's website, but to summarize, the dataset has the following variables:

Community Area Number (ca): Used to uniquely identify each row of the dataset

Community Area Name (community_area_name): The name of the region in the city of Chicago

Percent of Housing Crowded (percent_of_housing_crowded): Percent of occupied housing units with more than one person per room

Percent Households Below Poverty (percent_households_below_poverty): Percent of households living below the federal poverty line

Percent Aged 16+ Unemployed (percent_aged_16_unemployed): Percent of persons over the age of 16 years that are unemployed

Percent Aged 25+ without High School Diploma (percent_aged_25_without_high_school_diploma): Percent of persons over the age of 25 years without a high school education

Percent Aged Under 18 or Over 64:Percent of population under 18 or over 64 years of age (percent_aged_under_18_or_over_64): (ie. dependents)

Per Capita Income (per_capita_income_): Community Area per capita income is estimated as the sum of tract-level aggragate incomes divided by the total population

Hardship Index (hardship_index): Score that incorporates each of the six selected socioeconomic indicators

In this Lab, we'll take a look at the variables in the socioeconomic indicators dataset and do some basic analysis with Python.

Connect to the database
Let us first load the SQL extension and establish a connection with the database
'''
%load_ext sql

# Remember the connection string is of the format:
# %sql ibm_db_sa://my-username:my-password@my-hostname:my-port/my-db-name
# Enter the connection string for your Db2 on Cloud database instance below
# i.e. copy after db2:// from the URI string in Service Credentials of your Db2 instance. Remove the double quotes at the end.
%sql ibm_db_sa://smz55205:db8-q34k6b85vnrq@dashdb-txn-sbox-yp-dal09-11.services.dal.bluemix.net:50000/BLUDB

''''
Store the dataset in a Table
In many cases the dataset to be analyzed is available as a .CSV (comma separated values) file, perhaps on the internet. To analyze the data using SQL, it first needs to be stored in the database.
We will first read the dataset source .CSV from the internet into pandas dataframe
Then we need to create a table in our Db2 database to store the dataset. The PERSIST command in SQL "magic" simplifies the process of table creation and writing the data from a pandas dataframe into the table
'''
import pandas
chicago_socioeconomic_data = pandas.read_csv('https://data.cityofchicago.org/resource/jcxq-k9xf.csv')
%sql PERSIST chicago_socioeconomic_data

#You can verify that the table creation was successful by making a basic query like:
%sql SELECT * FROM chicago_socioeconomic_data limit 5;

#How many rows are in the dataset?
%sql SELECT COUNT(*) FROM chicago_socioeconomic_data;

#How many community areas in Chicago have a hardship index greater than 50.0?
%sql SELECT COUNT(*) FROM chicago_socioeconomic_data WHERE hardship_index > 50.0;

#What is the maximum value of hardship index in this dataset?
%sql SELECT MAX(hardship_index) FROM chicago_socioeconomic_data;

#Which community area which has the highest hardship index?
%sql SELECT community_area_name FROM chicago_socioeconomic_data where hardship_index=98.0

#or another option:
%sql SELECT community_area_name FROM chicago_socioeconomic_data ORDER BY hardship_index DESC NULLS LAST FETCH FIRST ROW ONLY;

#or you can use a sub-query to determine the max hardship index:
%sql select community_area_name from chicago_socioeconomic_data where hardship_index = ( select max(hardship_index) from chicago_socioeconomic_data ) 

#Which Chicago community areas have per-capita incomes greater than $60,000?
%sql SELECT community_area_name FROM chicago_socioeconomic_data WHERE per_capita_income_ > 60000;

#Create a scatter plot using the variables per_capita_income_ and hardship_index. Explain the correlation between the two variables.
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

income_vs_hardship = %sql SELECT per_capita_income_, hardship_index FROM chicago_socioeconomic_data;
plot = sns.jointplot(x='per_capita_income_',y='hardship_index', data=income_vs_hardship.DataFrame())

''''
Conclusion
Now that you know how to do basic exploratory data analysis using SQL and python visualization tools, you can further explore this dataset to see how the variable per_capita_income_ is related to percent_households_below_poverty and percent_aged_16_unemployed. Try to create interesting visualizations!
'''