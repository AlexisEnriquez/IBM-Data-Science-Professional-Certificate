# Course 9
# Data Visualization with Python
# 7- Dash Basics

''''
Dash Components
Objectives
Create a dash application layout
Add HTML H1, P, and Div components
Add core graph component
Add multiple charts
Dataset Used
Airline Reporting Carrier On-Time Performance dataset from Data Asset eXchange

Lab Questions
We will be using the same pie and sunburst chart theme from Plotly basics lab.

Theme for Pie Chart

Proportion of distance group (250 mile distance interval group) by month (month indicated by numbers).

Theme for Sunburst Chart

Hierarchical view in othe order of month and destination state holding value of number of flights.
'''

# Import required packages
import pandas as pd
import plotly.express as px

#Load the data
# Read the airline data into pandas dataframe
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

#Proportion of distance group (250 mile distance interval group) by month (month indicated by numbers).
# Pie Chart Creation
fig = px.pie(data, values='Month', names='DistanceGroup', title='Distance group proportion by month')
fig.show()

''''
Let's start creating dash application
Theme
Proportion of distance group (250 mile distance interval group) by month (month indicated by numbers).

To do:
Import required libraries and create an application layout
Add title to the dashboard using HTML H1 component
Add a paragraph about the chart using HTML P component
Add the pie chart created above using core graph component
Run the app
'''

''''
Hints
General examples can be found here.

For step 1 (only review), this is very specific to running app from Jupyerlab.

For Jupyterlab,we will be using jupyter-dash library. Adding from jupyter_dash import JupyterDash import statement.
Instead of creating dash application using app = dash.Dash(), we will be using app = JupyterDash(__name__).
For step 2,

Plotly H1 HTML Component
Title as Airline Performance Dashboard
Use style parameter and make the title center aligned, with color code #503D36, and font-size as 40. Check More about HTML section here.
For step 3,

Plotly Paragraph Component
Paragraph as Proportion of distance group (250 mile distance interval group) by month (month indicated by numbers).
Use style parameter to make the description center aligned and with color #F57241.
For step 4, refer dcc.Graph component usage.

For step 5, you can refer examples provided here.

NOTE: Run the solution cell multiple times if you are not seeing the result.

App Skeleton
import dash

from jupyter_dash import JupyterDash


app = JupyterDash(__name__)
JupyterDash.infer_jupyter_proxy_config()


app.layout = html.Div(children=[html.H1(.......),
                                html.P(.......),
                                dcc.Graph(......)
                               ]
                      )
if __name__ == '__main__':
    app.run_server(mode="inline", host="localhost") 
'''
# Import required libraries
import dash
import dash_html_components as html
import dash_core_components as dcc
from jupyter_dash import JupyterDash

JupyterDash.infer_jupyter_proxy_config()

# needs to be run again in a separate cell due to a jupyterdash bug
JupyterDash.infer_jupyter_proxy_config()


# Import required libraries
import dash
import dash_html_components as html
import dash_core_components as dcc
from jupyter_dash import JupyterDash

# Create a dash application
app = JupyterDash(__name__)
JupyterDash.infer_jupyter_proxy_config()

# Get the layout of the application and adjust it.
# Create an outer division using html.Div and add title to the dashboard using html.H1 component
# Add description about the graph using HTML P (paragraph) component
# Finally, add graph component.
app.layout = html.Div(children=[html.H1('Airline Dashboard', 
                                         style={'textAlign': 'center',
                                                'color': '#503D36',
                                                 'font-size': 40}),
                                html.P('Proportion of distance group (250 mile distance interval group) by month (month indicated by numbers).',
                                        style={'textAlign':'center', 'color': '#F57241'}),
                                dcc.Graph(figure=fig),
                                               
                    ])
if __name__ == '__main__':
    app.run_server(mode="inline", host="localhost")