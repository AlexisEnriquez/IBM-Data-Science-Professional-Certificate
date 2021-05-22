# Course 9
# Data Visualization with Python
# 6- Plotly basics: scatterm line, bar, bubble, histogram, pie, sunburst

''''
Basic Plotly Charts
Estimated time needed: 30 minutes

Objectives
In this lab, you will learn about creating plotly charts using plotly.graph_objects and plotly.express.

Learn more about:

Plotly python
Plotly Graph Objects
Plotly Express
Handling data using Pandas
We will be using the airline dataset from Data Asset eXchange.

Airline Reporting Carrier On-Time Performance Dataset
The Reporting Carrier On-Time Performance Dataset contains information on approximately 200 million domestic US flights reported to the United States Bureau of Transportation Statistics. The dataset contains basic information about each flight (such as date, time, departure airport, arrival airport) and, if applicable, the amount of time the flight was delayed and information about the reason for the delay. This dataset can be used to predict the likelihood of a flight arriving on time.

Preview data, dataset metadata, and data glossary here.
'''
# Import required libraries
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

#Real Data
# Read the airline data into pandas dataframe
airline_data =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv', 
                            encoding = "ISO-8859-1",
                            dtype={'Div1Airport': str, 'Div1TailNum': str, 
                                   'Div2Airport': str, 'Div2TailNum': str})

# Preview the first 5 lines of the loaded data 
airline_data.head()

# Shape of the data
airline_data.shape

# Randomly sample 500 data points. Setting the random state to be 42 so that we get same result.
data = airline_data.sample(n=500, random_state=42)

# Get the shape of the trimmed data
data.shape

''''
Lab structure
plotly.graph_objects
Review scatter plot creation

Theme: How departure time changes with respect to airport distance

To do - Create line plot

Theme: Extract average monthly delay time and see how it changes over the year

plotly.express
Review bar chart creation

Theme: Extract number of flights from a specific airline that goes to a destination

To do - Create bubble chart

Theme: Get number of flights as per reporting airline

To do - Create histogram

Theme: Get distribution of arrival delay

Review pie chart

Theme: Proportion of distance group by month (month indicated by numbers)

To do - Create sunburst chart

Theme: Hierarchical view in othe order of month and destination state holding value of number of flights
'''

#plotly.graph_objects
#1. Scatter Plot
#Learn more about usage of scatter plot here

#Idea: How departure time changes with respect to airport distance
# First we create a figure using go.Figure and adding trace to it through go.scatter
fig = go.Figure(data=go.Scatter(x=data['Distance'], y=data['DepTime'], mode='markers', marker=dict(color='red')))
# Updating layout through `update_layout`. Here we are adding title to the plot and providing title to x and y axis.
fig.update_layout(title='Distance vs Departure Time', xaxis_title='Distance', yaxis_title='DepTime')
# Display the figure
fig.show()

#2. Line Plot
#Learn more about line plot here

#Idea: Extract average monthly arrival delay time and see how it changes over the year.
# Group the data by Month and compute average over arrival delay time.
line_data = data.groupby('Month')['ArrDelay'].mean().reset_index()
# Display the data
line_data

#To do:
#Create a line plot with x-axis being the month and y-axis being computed average delay time. Update plot title,
#xaxis, and yaxis title.
#Hint: Scatter and line plot vary by updating mode parameter.

fig = go.Figure(data=go.Scatter(x=line_data['Month'], y=line_data['ArrDelay'], mode='lines', marker=dict(color='green')))
fig.update_layout(title='Month vs Average Flight Delay Time', xaxis_title='Month', yaxis_title='ArrDelay')
fig.show()

#plotly.express
#1. Bar Chart
#Learn more about bar chart here

#Idea: Extract number of flights from a specific airline that goes to a destination
# Group the data by destination state and reporting airline. Compute total number of flights in each combination
bar_data = data.groupby(['DestState'])['Flights'].sum().reset_index()
# Display the data
bar_data
# Use plotly express bar chart function px.bar. Provide input data, x and y axis variable, and title of the chart.
# This will give total number of flights to the destination state.
fig = px.bar(bar_data, x="DestState", y="Flights", title='Total number of flights to the destination state split by reporting airline') 
fig.show()

#2. Bubble Chart
Idea: Get number of flights as per reporting airline
# Group the data by reporting airline and get number of flights
bub_data = data.groupby('Reporting_Airline')['Flights'].sum().reset_index()
bub_data
''''
To do

Create a bubble chart using the bub_data with x-axis being reporting airline and y-axis being flights.
Provide title to the chart
Update size of the bubble based on the number of flights. Use size parameter.
Update name of the hover tooltip to reporting_airline using hover_name parameter.
'''
fig = px.scatter(bub_data, x="Reporting_Airline", y="Flights", size="Flights",
                 hover_name="Reporting_Airline", title='Reporting Airline vs Number of Flights', size_max=60)
fig.show()

''''
Histogram
Learn more about histogram here

Idea: Get distribution of arrival delay
'''
# Set missing values to 0
data['ArrDelay'] = data['ArrDelay'].fillna(0)

#To do

#Use px.histogram and pass the dataset.
#Pass ArrDelay to x parameter.
fig = px.histogram(data, x="ArrDelay")
fig.show()

''''
Pie Chart
Learn more about pie chart here

Idea: Proportion of distance group by month (month indicated by numbers)
'''
# Use px.pie function to create the chart. Input dataset. 
# Values parameter will set values associated to the sector. 'Month' feature is passed to it.
# labels for the sector are passed to the `names` parameter.
fig = px.pie(data, values='Month', names='DistanceGroup', title='Distance group proportion by month')
fig.show()

''''
Sunburst Charts
Learn more about sunburst chart here

Idea: Hierarchical view in othe order of month and destination state holding value of number of flights
To do

Create sunburst chart using px.sunburst.
Define hierarchy of sectors from root to leaves in path parameter. Here, we go from Month to DestStateName feature.
Set sector values in values paramter. Here, we can pass in Flights feature.
Show the figure.
'''
fig = px.sunburst(data, path=['Month', 'DestStateName'], values='Flights')
fig.show()
