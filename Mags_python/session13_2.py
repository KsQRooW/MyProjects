# -*- coding: utf-8 -*-
"""
dash multi-page apps

pip3 install dash --upgrade

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

# # Простейший пример с печать изменений URL
# # Пример перехода
# from dash import Dash, dcc, html, callback, Input, Output
#
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#
# app = Dash(__name__, external_stylesheets=external_stylesheets)
# app.title = "Пример"
# app.layout = html.Div([
#     # represents the browser address bar and doesn't render anything
#     dcc.Location(id='url', refresh=False),
#
#     dcc.Link('Navigate to home', href='/', refresh=False),
#     html.Br(),
#     dcc.Link('Navigate to "Page 1"', href='/page-1', refresh=False),
#     # dcc.Link('Navigate to "Page 1"', href='https://mail.ru/', refresh=True),
#
#     # content will be rendered in this element
#     html.Div(id='page-content', className="table-1")
# ])
#
#
# @callback(Output('page-content', 'children'),
#               [Input('url', 'pathname')])
# def display_page(pathname):
#     return html.Div([
#         html.H3(f'You are on page {pathname}')
#     ])
#
#
# if __name__ == '__main__':
#     app.run_server(debug=True)
    
#--------------------------------------------------------------------
    
# # Показ разных страниц
# """
# Since we're adding callbacks to elements that don't exist in
# the app.layout, Dash will raise an exception to warn us that we
# might be doing something wrong. In this case, we're adding the
# elements through a callback, so we can ignore the exception by
# setting suppress_callback_exceptions=True. I
# """
# from dash import Dash, dcc, html, Input, Output, callback
#
# app = Dash(__name__, suppress_callback_exceptions=True)
#
# app.layout = html.Div([
#     dcc.Location(id='url', refresh=False),
#     html.Div(id='page-content')
# ])
#
#
# index_page = html.Div([
#     dcc.Link('Go to Page 1', href='/page-1'),
#     html.Br(),
#     dcc.Link('Go to Page 2', href='/page-2'),
# ])
#
# page_1_layout = html.Div([
#     html.H1('Page 1'),
#     dcc.Dropdown(['LA', 'NYC', 'MTL'], 'LA', id='page-1-dropdown'),
#     html.Div(id='page-1-content'),
#     html.Br(),
#     dcc.Link('Go to Page 2', href='/page-2'),
#     html.Br(),
#     dcc.Link('Go back to home', href='/'),
# ])
#
# @callback(Output('page-1-content', 'children'),
#               [Input('page-1-dropdown', 'value')])
# def page_1_dropdown(value):
#     return f'You have selected {value}'
#
#
# page_2_layout = html.Div([
#     html.H1('Page 2'),
#     dcc.RadioItems(['Orange', 'Blue', 'Red'], 'Orange', id='page-2-radios'),
#     html.Div(id='page-2-content'),
#     html.Br(),
#     dcc.Link('Go to Page 1', href='/page-1'),
#     html.Br(),
#     dcc.Link('Go back to home', href='/')
# ])
#
# @callback(Output('page-2-content', 'children'),
#               [Input('page-2-radios', 'value')])
# def page_2_radios(value):
#     return f'You have selected {value}'
#
#
# # Update the index
# @callback(Output('page-content', 'children'),
#               [Input('url', 'pathname')])
# def display_page(pathname):
#     if pathname == '/page-1':
#         return page_1_layout
#     elif pathname == '/page-2':
#         return page_2_layout
#     else:
#         return index_page
#     # You could also return a 404 "URL not found" page here
#
# if __name__ == '__main__':
#     app.run_server(debug=True)

#--------------------------------------------------------------------
    
# # Показ разных страниц
# # Импорт Layout из файла
# """
# Since we're adding callbacks to elements that don't exist in
# the app.layout, Dash will raise an exception to warn us that we
# might be doing something wrong. In this case, we're adding the
# elements through a callback, so we can ignore the exception by
# setting suppress_callback_exceptions=True. I
# """
# from dash import Dash, dcc, html, Input, Output, callback
# from dash_layouts import page_1_layout, page_2_layout
#
#
# app = Dash(__name__, suppress_callback_exceptions=True)
#
# app.layout = html.Div([
#     dcc.Location(id='url', refresh=False),
#     html.Div(id='page-content', className="table-1")
# ])
#
#
# index_page = html.Div([
#     dcc.Link('Go to Page 1', href='/page-1'),
#     html.Br(),
#     dcc.Link('Go to Page 2', href='/page-2'),
# ])
#
#
# @callback(Output('page-1-content', 'children'),
#               [Input('page-1-dropdown', 'value')])
# def page_1_dropdown(value):
#     return f'You have selected {value}'
#
#
# @callback(Output('page-2-content', 'children'),
#               [Input('page-2-radios', 'value')])
# def page_2_radios(value):
#     return f'You have selected {value}'
#
#
# # Update the index
# @callback(Output('page-content', 'children'),
#               [Input('url', 'pathname')])
# def display_page(pathname):
#     if pathname == '/page-1':
#         return page_1_layout
#     elif pathname == '/page-2':
#         return page_2_layout
#     else:
#         return index_page
#     # You could also return a 404 "URL not found" page here
#
# if __name__ == '__main__':
#     app.run_server(debug=True)

#--------------------------------------------------------------------
    
# Проверка корректности callback
# СОбираем интерфейс для проверки
from dash import Dash, html, dcc, Input, Output, State, callback

app = Dash(__name__)
app.title = "Пример"
url_bar_and_content_div = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

layout_index = html.Div([
    dcc.Link('Navigate to "/page-1"', href='/page-1'),
    html.Br(),
    dcc.Link('Navigate to "/page-2"', href='/page-2'),
])

layout_page_1 = html.Div([
    html.H2('Page 1'),
    dcc.Input(id='input-1-state', type='text', value='Montreal'),
    dcc.Input(id='input-2-state', type='text', value='Canada'),
    html.Button(id='submit-button', n_clicks=0, children='Submit'),
    html.Div(id='output-state'),
    html.Br(),
    dcc.Link('Navigate to "/"', href='/'),
    html.Br(),
    dcc.Link('Navigate to "/page-2"', href='/page-2'),
])

layout_page_2 = html.Div([
    html.H2('Page 2'),
    dcc.Dropdown(['LA', 'NYC', 'MTL'], 'LA', id='page-2-dropdown'),
    html.Div(id='page-2-display-value'),
    html.Br(),
    dcc.Link('Navigate to "/"', href='/'),
    html.Br(),
    dcc.Link('Navigate to "/page-1"', href='/page-1'),
])

# index layout
app.layout = url_bar_and_content_div

# "complete" layout
app.validation_layout = html.Div([
    url_bar_and_content_div,
    layout_index,
    layout_page_1,
    layout_page_2,
])


# Index callbacks
@callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == "/page-1":
        return layout_page_1
    elif pathname == "/page-2":
        return layout_page_2
    else:
        return layout_index


# Page 1 callbacks
@callback(Output('output-state', 'children'),
              Input('submit-button', 'n_clicks'),
              State('input-1-state', 'value'),
              State('input-2-state', 'value'))
def update_output(n_clicks, input1, input2):
    return f'The Button has been pressed {n_clicks} times. \
            Input 1 is {input1} and Input 2 is {input2}'


# Page 2 callbacks
@callback(Output('page-2-display-value', 'children'),
              Input('page-2-dropdown', 'value'))
def display_value(value):
    return f'You have selected {value}'


if __name__ == '__main__':
    app.run_server(debug=True)
