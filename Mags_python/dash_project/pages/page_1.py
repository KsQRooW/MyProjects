from dash import dcc, html
import plotly.express as px
from dash.dependencies import Input, Output
from Mags_python.dash_project.settings import app, df

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
            value='children', className="dropdown", style={'margit-bottom': '32px'}
        ), dcc.Graph(id='output_graph')], className="card")]
