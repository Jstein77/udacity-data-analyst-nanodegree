import pandas as pd
import numpy as np
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as FF
plotly.tools.set_credentials_file(username='JordanStein', api_key='hAdgKhJyKLgGEdt95qe1')


#Read data from csv
sf_temps = pd.read_csv("/Users/jordanstein/udacity-data-analyst-nanodegree/Udacity/City_data.csv")
world_temps = pd.read_csv("/Users/jordanstein/udacity-data-analyst-nanodegree/Udacity/global_data.csv")


sample_table = FF.create_table(sf_temps.head())
py.iplot(sample_table, filename = 'sample_table')

trace1 = go.Scatter(
                    x=sf_temps['year'], y=sf_temps['avg_temp'], # Data
                    mode='lines', name='5yr average San Francisco' # Additional options
                   )

trace2 = go.Scatter(
                    x=world_temps['year'], y=world_temps['avg_temp'], # Data
                    mode='lines', name='5yr average World' # Additional options
                   )

layout = go.Layout(title='Average temprature',
    xaxis=dict(
        title='Year',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='Temperature',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
                   plot_bgcolor='rgb(230, 230,230)')

fig = go.Figure(data=[trace1, trace2], layout=layout)
py.iplot(fig, filename='Average temprature')
