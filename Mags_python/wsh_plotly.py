# -*- coding: utf-8 -*-
"""
Изучаем plotly 
visit http://127.0.0.1:8050/ in your web browser.
"""

import dash
from dash import Dash, Output, Input
import dash_html_components as html
import dash_core_components as dcc
import dash_renderer as drnd
import dash_table as tbl
import plotly.express as px
from dash.exceptions import PreventUpdate
from plotly.subplots import make_subplots
import plotly.graph_objs as go
import pandas as pd

# Элементарный callback
# app = Dash(__name__)
# # type = "text", "number", "password", "email", "search", "tel", "url",
# # "range", "hidden"
# # При наведении мыши - подсказка

# app.layout = html.Div([
#     html.H6("Change the value in the text box to see callbacks in action!"),
#     html.Div([
#         "Input: ",
#         dcc.Input(id='my-input', value='initial value', type='text')
#     ]),
#     html.Br(),
#     html.Div(id='my-output'),
#
# ])
#
# # Декоратор - определяет условия запуска на счет функции:
# # входные парамтеры и направление выхода
# @app.callback(
#     Output(component_id='my-output', component_property='children'),
#     Input(component_id='my-input', component_property='value')
# )
# def update_output_div(input_value):
#     return f'Output: {input_value}'
#
#
# if __name__ == '__main__':
#     app.run_server(debug=True)

# # # # # # # # # # #

# # Вариант простого callback с защитой от обновлений
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#
# app = Dash(__name__, external_stylesheets=external_stylesheets)
#
# app.layout = html.Div([
#     html.Button('Click here to see the content', id='show-secret'),
#     html.Div(id='body-div')
# ])
#
# @app.callback(
#     Output(component_id='body-div', component_property='children'),
#     Input(component_id='show-secret', component_property='n_clicks')
# )
# def update_output(n_clicks):
#     if n_clicks is None:
#         raise PreventUpdate # Защита от обновлений
#     else:
#         return "Elephants are the only animal that can't jump"
#
#
# if __name__ == '__main__':
#     app.run_server(debug=True)

# # # # # # # #

# # Выпадающий список
# app = Dash(__name__)
# app.layout = html.Div([
#     dcc.Dropdown(['NYC', 'MTL', 'SF'], 'NYC', id='demo-dropdown'),
#     html.Div(id='dd-output-container')
# ])
#
#
# @app.callback(
#     Output('dd-output-container', 'children'),
#     Input('demo-dropdown', 'value')
# )
# def update_output(value):
#     return f'You have selected {value}'
#
#
# if __name__ == '__main__':
#     app.run_server(debug=True)

# # # # # # # # # #

# # Сложный callback график с выбором данных
# df = pd.read_excel("AUTO21053A.xlsx")
#
# app = Dash(__name__)
#
# app.layout = html.Div([
#     dcc.Graph(id='selected-graph'),
#     "Выбор аргумента",
#     dcc.Dropdown(df.columns, df.columns[0], placeholder="Выбор аргумента",
#                   id='x'),
#     "Выбор функции",
#     dcc.Dropdown(df.columns, df.columns[0], placeholder="Выбор функции",
#                   id='y')
# ])
#
# @app.callback(
#     Output('selected-graph', 'figure'),
#     Input('x', 'value'),
#     Input('y', 'value'))
# def update_figure(x_name, y_name):
#     fig = px.scatter(df, x=x_name, y=y_name, log_x=True)
#     fig.update_layout(transition_duration=500)
#     return fig
#
#
# if __name__ == '__main__':
#     app.run_server(debug=True)

# # # # # # # # # #

# # Сложный callback график со слайдером.
# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
#
# app = Dash(__name__)
#
# app.layout = html.Div([
#     dcc.Graph(id='graph-with-slider'),
#     dcc.Slider(
#         df['year'].min(),
#         df['year'].max(),
#         step=None,
#         value=df['year'].min(),
#         marks={str(year): str(year) for year in df['year'].unique()},
#         id='year-slider'
#     )
# ])
#
#
# @app.callback(
#     Output('graph-with-slider', 'figure'),
#     Input('year-slider', 'value'))
# def update_figure(selected_year):
#     filtered_df = df[df.year == selected_year]
#
#     fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
#                       size="pop", color="continent", hover_name="country",
#                       log_x=True, size_max=55)
#
#     fig.update_layout(transition_duration=500)
#
#     return fig
#
#
# if __name__ == '__main__':
#     app.run_server(debug=True)
