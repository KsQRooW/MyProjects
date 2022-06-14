from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
# import dash_html_components as html
# import dash_core_components as dcc
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd

page_1 = [
    html.Div(
        children=[
            html.H1(children='Analysis diamonds dataset', className='header-title'),

            html.P(children='maybe this demo will be useful to someone (:', className='header-description')
        ], className='header'),

    html.Div([
        dcc.Dropdown(
            id='demo_drop',
            options=[
                {'label': 'Количество детей', 'value': 'children'},
                {'label': 'Charges', 'value': 'charges'},
                {'label': 'BMI', 'value': 'bmi'}
            ],
            value='charges', className="dropdown", style={'margit-bottom': '32px'}
        ), dcc.Graph(id='output_graph')], className="card")]
