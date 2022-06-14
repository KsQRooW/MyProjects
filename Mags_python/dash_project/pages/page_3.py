from dash import Dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd

page_3 = [
    html.Div(
        children=[
            html.H1(children='Thank you for your attention! :)', className='header-title'),

        ], className='header')
]
