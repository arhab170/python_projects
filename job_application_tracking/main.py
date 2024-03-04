#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib as plt
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import os
import datetime


# In[22]:


# Full time tech
# Define the path to the directory
directory_path = r'G:\My Drive\Application Documents\1 Data Science\Applications\full time'

# Function to get creation date of a file or directory
def get_creation_date(path):
    return datetime.datetime.fromtimestamp(os.path.getctime(path))

# List all folders (directories) in the specified directory along with their creation dates
folders_with_dates = [(f.name, get_creation_date(f.path)) for f in os.scandir(directory_path) if f.is_dir()]

# Create a DataFrame from the list
df = pd.DataFrame(folders_with_dates, columns=['Folder Name', 'Creation Date'])
df["Field"] = "Tech"
df["Type"] = "Full time"


# In[23]:


directory_path = r'G:\My Drive\Application Documents\1 Data Science\Applications\werkstudent'

# Function to get creation date of a file or directory
def get_creation_date(path):
    return datetime.datetime.fromtimestamp(os.path.getctime(path))

# List all folders (directories) in the specified directory along with their creation dates
folders_with_dates = [(f.name, get_creation_date(f.path)) for f in os.scandir(directory_path) if f.is_dir()]

# Create a DataFrame from the list
temp_df = pd.DataFrame(folders_with_dates, columns=['Folder Name', 'Creation Date'])
temp_df["Field"] = "Tech"
temp_df["Type"] = "Part time"

df = pd.concat([df, temp_df], ignore_index=True)


# In[ ]:


directory_path = r'G:\My Drive\Application Documents\1 Data Science\Applications\werkstudent'

# Function to get creation date of a file or directory
def get_creation_date(path):
    return datetime.datetime.fromtimestamp(os.path.getctime(path))

# List all folders (directories) in the specified directory along with their creation dates
folders_with_dates = [(f.name, get_creation_date(f.path)) for f in os.scandir(directory_path) if f.is_dir()]

# Create a DataFrame from the list
temp_df = pd.DataFrame(folders_with_dates, columns=['Folder Name', 'Creation Date'])
temp_df["Field"] = "Tech"
temp_df["Type"] = "Part time"


# In[25]:


directory_path = r'G:\My Drive\Application Documents\1.1 Climate Tech\Applications'

# Function to get creation date of a file or directory
def get_creation_date(path):
    return datetime.datetime.fromtimestamp(os.path.getctime(path))

# List all folders (directories) in the specified directory along with their creation dates
folders_with_dates = [(f.name, get_creation_date(f.path)) for f in os.scandir(directory_path) if f.is_dir()]

# Create a DataFrame from the list
temp_df = pd.DataFrame(folders_with_dates, columns=['Folder Name', 'Creation Date'])
temp_df["Field"] = "Climate Tech"
temp_df["Type"] = "Full time"

df = pd.concat([df, temp_df], ignore_index=True)
df


# In[26]:


directory_path = r'G:\My Drive\Application Documents\2 Sustainability\Applications'

# Function to get creation date of a file or directory
def get_creation_date(path):
    return datetime.datetime.fromtimestamp(os.path.getctime(path))

# List all folders (directories) in the specified directory along with their creation dates
folders_with_dates = [(f.name, get_creation_date(f.path)) for f in os.scandir(directory_path) if f.is_dir()]

# Create a DataFrame from the list
temp_df = pd.DataFrame(folders_with_dates, columns=['Folder Name', 'Creation Date'])
temp_df["Field"] = "Sustainability"
temp_df["Type"] = "Full time"

df = pd.concat([df, temp_df], ignore_index=True)
df


# In[27]:


# Initialize the Dash app
app = dash.Dash(__name__)

# Create dropdown filters for each column
dropdowns = html.Div([
    html.Label('Select a value for "Field":'),
    dcc.Dropdown(
        id='field-dropdown',
        options=[{'label': i, 'value': i} for i in df['Field'].unique()],
        value=None
    ),
    html.Label('Select a value for "Value":'),
    dcc.Dropdown(
        id='value-dropdown',
        options=[{'label': i, 'value': i} for i in df['Value'].unique()],
        value=None
    )
])

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1("Data Visualization with Filters"),
    dropdowns,
    dcc.Graph(id='graph')
])

# Define callback to update the graph
@app.callback(
    Output('graph', 'figure'),
    [Input('field-dropdown', 'value'),
     Input('value-dropdown', 'value')]
)
def update_graph(selected_field, selected_value):
    filtered_df = df

    if selected_field:
        filtered_df = filtered_df[filtered_df['Field'] == selected_field]
    if selected_value:
        filtered_df = filtered_df[filtered_df['Value'] == selected_value]

    counts = filtered_df['Field'].value_counts()

    return {
        'data': [
            {'x': counts.index, 'y': counts.values, 'type': 'bar', 'name': 'Count'},
        ],
        'layout': {
            'title': 'Count of Different String Values',
            'xaxis': {'title': 'String Values'},
            'yaxis': {'title': 'Count'}
        }
    }

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
# %%
