import pandas as pd
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

import os
URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv"
spacex_df = pd.read_csv("data/spacex_launch_dash.csv" if os.path.exists("data/spacex_launch_dash.csv") else URL)
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()
sites = spacex_df['Launch Site'].unique()

app = dash.Dash(__name__)
app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard', style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
    # TASK 1: Launch site drop-down
    dcc.Dropdown(id='site-dropdown',
                 options=[{'label': 'All Sites', 'value': 'ALL'}] + [{'label': s, 'value': s} for s in sites],
                 value='ALL', placeholder="Select a Launch Site here", searchable=True),
    html.Br(),
    # TASK 2: Pie chart
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),
    html.P("Payload range (Kg):"),
    # TASK 3: Range slider
    dcc.RangeSlider(id='payload-slider', min=0, max=10000, step=1000,
                    marks={i: str(i) for i in range(0, 10001, 2500)},
                    value=[min_payload, max_payload]),
    # TASK 4: Scatter chart
    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])

@app.callback(Output('success-pie-chart', 'figure'), Input('site-dropdown', 'value'))
def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        data = spacex_df.groupby('Launch Site')['class'].sum().reset_index()
        return px.pie(data, values='class', names='Launch Site', title='Total Successful Launches by Site')
    data = spacex_df[spacex_df['Launch Site'] == entered_site]['class'].value_counts().reset_index()
    data.columns = ['class', 'count']
    data['Outcome'] = data['class'].map({1: 'Success (1)', 0: 'Failure (0)'})
    return px.pie(data, values='count', names='Outcome', title=f'Total Success vs. Failure Launches for site {entered_site}')

@app.callback(Output('success-payload-scatter-chart', 'figure'),
              [Input('site-dropdown', 'value'), Input('payload-slider', 'value')])
def get_scatter_chart(entered_site, payload_range):
    low, high = payload_range
    data = spacex_df[(spacex_df['Payload Mass (kg)'] >= low) & (spacex_df['Payload Mass (kg)'] <= high)]
    title = 'Correlation between Payload and Success for all Sites'
    if entered_site != 'ALL':
        data = data[data['Launch Site'] == entered_site]
        title = f'Correlation between Payload and Success for site {entered_site}'
    return px.scatter(data, x='Payload Mass (kg)', y='class', color='Booster Version Category', title=title)

if __name__ == '__main__':
    app.run(port=8060)
