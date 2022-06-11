# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 12:46:40 2022

@author: polya
"""
import os
import dash
from dash import Dash, html, dcc
from dash import dash_table as tbl
# Не путать с html.Output и dcc.Input
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import plotly.express as px
import pandas as pd

page_1_layout = html.Div([
    html.H1('Page 1'),
    dcc.Dropdown(['LA', 'NYC', 'MTL'], 'LA', id='page-1-dropdown'),
    html.Div(id='page-1-content'),
    html.Br(),
    dcc.Link('Go to Page 2', href='/page-2'),
    html.Br(),
    dcc.Link('Go back to home', href='/'),
])

page_2_layout = html.Div([
    html.H1('Page 2'),
    dcc.RadioItems(['Orange', 'Blue', 'Red'], 'Orange', id='page-2-radios'),
    html.Div(id='page-2-content'),
    html.Br(),
    dcc.Link('Go to Page 1', href='/page-1'),
    html.Br(),
    dcc.Link('Go back to home', href='/')
])
