# -*- coding: utf-8 -*-
"""
Изучение Plotly DASH
"""
import os
os.chdir("d:/work.p/")
from dash import Dash, Input, Output
import dash_html_components as html
import dash_core_components as dcc
import dash_renderer as drnd
import dash_table as tbl
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# # 1 app layout 
# df = pd.DataFrame({
#     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
#     "Amount": [4, 1, 2, 2, 4, 5],
#     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
# })

# fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# app.layout = html.Div([
#     html.H1(children='Привет!'),

#     html.Div('''
#         Dash: Web среда для данных
#     '''),

#     dcc.Graph(
#         id='example-graph',
#         figure=fig
#     )
# ])

# # 2 app layout 

# colors = {
#     'background': '#00AACC',
#     'text': '#7FDBFF'
# }

# # 2 app layout 

# df = pd.DataFrame({
#     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
#     "Amount": [4, 1, 2, 2, 4, 5],
#     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
# })

# fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# fig.update_layout(
#     plot_bgcolor=colors['background'],
#     paper_bgcolor=colors['background'],
#     font_color=colors['text']
# )

# app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
#     html.H1(
#         children='Hello Dash',
#         style={
#             'textAlign': 'center',
#             'color': colors['text']
#         }
#     ),

#     html.Div(children='Dash: A web application framework for your data.', style={
#         'textAlign': 'center',
#         'color': colors['text']
#     }),

#     dcc.Graph(
#         id='example-graph-2',
#         figure=fig
#     )
# ])

# 3 Interaction
app.layout = html.Div([
    html.H6("Change the value in the text box to see callbacks in action!"),
    html.Div([
        "Input: ",
        dcc.Input(id='my-input', value='initial value', type='text')
    ]),
    html.Br(),
    html.Div(id='my-output'),

])


@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
def update_output_div(input_value):
    return f'Output: {input_value}'
           
if __name__ == '__main__':
    app.run_server(debug=False)
