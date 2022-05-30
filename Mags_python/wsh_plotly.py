# -*- coding: utf-8 -*-
"""
Изучаем plotly 
visit http://127.0.0.1:8050/ in your web browser.
"""

import dash
from dash import Dash
import dash_html_components as html
import dash_core_components as dcc
import dash_renderer as drnd
import dash_table as tbl
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objs as go
import pandas as pd

app = Dash(__name__)

# С помощью классов
app.layout = html.Div([
    html.Div([
        'LEFT',
        html.Br(),
        'LEFT'
    ],
        id='t1'),
    html.Div([
        'Right',
        html.Br(),
        'Right'
    ],
        id='t2')
])

if __name__ == '__main__':
    app.run_server(debug=True)
