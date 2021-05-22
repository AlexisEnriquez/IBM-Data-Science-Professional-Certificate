# Course 9
# Data Visualization with Python
# 8- Dash Add interactivity: user input and callbacks

''''
Objectives
In this lab, you will work on Dash Callbacks.

Dataset Used
Airline Reporting Carrier On-Time Performance dataset from Data Asset eXchange

Lab Question
Extract average monthly arrival delay time and see how it changes over the year.

Dash Application Creation
Todo for the lab question
Import required libraries, read the airline data, and create an application layout
Add title to the dashboard using HTML H1 component
Add a HTML division and core text input component inside the division. Provide an input component id and a default value to the component.
Add a HTML dividion and core graph component. Provide a graph component id.
Add callback decorator and provide input and output parameters.
Define callback function, perform computation to extract required information, create the graph, and update the layout.
Run the app
Hints
General examples can be found here.

For step 1 (only review), this is very specific to running app from Jupyerlab.

For Jupyterlab,we will be using jupyter-dash library. Adding from jupyter_dash import JupyterDash import statement.
Instead of creating dash application using app = dash.Dash(), we will be using app = JupyterDash(__name__).
Use pandas to read the airline data.
For step 2,

Plotly H1 HTML Component
Title as Airline Performance Dashboard
Use style parameter and make the title center aligned, with color code #503D36, and font-size as 40. Check More about HTML section here.
For step 3,

Add dcc input component and provide id as input-year. Use style parameter and assign height of the inout box to be 50px and font-size to be 35.
HTML Div component and provide id as line-plot. Use style parameter and assign font-size as 40.
For step 4,

Core graph component and assign id as line-plot.
For 5 and 6,

Basic callback
'''

''''
App Skeleton

import dash
....
....
from jupyter_dash import JupyterDash


app = JupyterDash(__name__)
JupyterDash.infer_jupyter_proxy_config()


app.layout = html.Div(children=[html.H1(.......),
                                html.Div(['Input:', dcc.Input(id='..', value='..', type='..', style={})], style={}),
                                html.Br(),
                                html.Br(),
                                html.Div(dcc.Graph(id='..')),
                               ])
                               
if __name__ == '__main__':
    app.run_server(mode="inline", host="localhost")
'''
# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from jupyter_dash import JupyterDash
import plotly.graph_objects as go
JupyterDash.infer_jupyter_proxy_config()
 # needs to be run again in a separate cell due to a jupyterdash bug
JupyterDash.infer_jupyter_proxy_config()

# Create a dash application
app = JupyterDash(__name__)

# Read the airline data into pandas dataframe
airline_data =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv', 
                            encoding = "ISO-8859-1",
                            dtype={'Div1Airport': str, 'Div1TailNum': str, 
                                   'Div2Airport': str, 'Div2TailNum': str})

# TODO
# Get the layout of the application and adjust it.
# Create an outer division using html.Div and add title to the dashboard using html.H1 component
# Add a html.Div and core input text component
# Finally, add graph component.
app.layout = html.Div(children=[ html.H1('Airline Performance Dashboard', 
                                style={'textAlign': 'center', 'color': '#503D36',
                                'font-size': 40}),
                                html.Div(["Input Year: ", dcc.Input(id='input-year', value='2010', 
                                type='number', style={'height':'50px', 'font-size': 35}),], 
                                style={'font-size': 40}),
                                html.Br(),
                                html.Br(),
                                html.Div(dcc.Graph(id='line-plot')),
                                ])

# add callback decorator
@app.callback( Output(component_id='line-plot', component_property='figure'),
               Input(component_id='input-year', component_property='value'))

# Add computation to callback function and return graph
def get_graph(entered_year):
    # Select 2019 data
    df =  airline_data[airline_data['Year']==int(entered_year)]
    
    # Group the data by Month and compute average over arrival delay time.
    line_data = df.groupby('Month')['ArrDelay'].mean().reset_index()

    fig = go.Figure(data=go.Scatter(x=line_data['Month'], y=line_data['ArrDelay'], mode='lines', marker=dict(color='green')))
    fig.update_layout(title='Month vs Average Flight Delay Time', xaxis_title='Month', yaxis_title='ArrDelay')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(mode="inline", host="localhost")