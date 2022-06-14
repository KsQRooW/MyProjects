from dash import Dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd

from Mags_python.dash_project.settings import df

page_2 = [
    html.Div(
        children=[
            html.H1('The effect of the carat on price', className='header-title',
                    style={'textAlign': 'center'})
        ], className='header'),
    dcc.Graph(id='graph1',
              figure=px.scatter(df, x='age',
                                y='charges'), className="card"),

    dcc.Graph(id='graph2',
              figure=px.scatter(df, x='age',
                                y='charges', facet_col='smoker'), className="card")
]
