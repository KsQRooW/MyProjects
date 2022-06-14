from dash import Dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd

SIDESTYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#222222",
}

CONTSTYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div([
    dcc.Location(id="url"),
    html.Div(
        [
            html.H6("Analyze", className="display-3", style={'color': 'white'}),
            html.Hr(style={'color': 'white'}),
            dbc.Nav(
                [
                    dbc.NavLink("Analysis", href="/page1", active="exact"),
                    dbc.NavLink("The effect", href="/page2", active="exact"),
                    dbc.NavLink("Thanks", href="/page3", active="exact"),
                ],
                vertical=True, pills=True),
        ],
        style=SIDESTYLE
    ),
    html.Div(id="page-content", children=[], style=CONTSTYLE)
])
