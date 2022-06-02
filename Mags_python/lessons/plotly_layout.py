# -*- coding: utf-8 -*-
"""
Изучение Plotly DASH
Run this app with `python app.py` and
visit http://127.0.0.1:8050/ in your web browser.
"""
import os
os.chdir("d:/work.p/scripts/html")
import dash
from dash import Dash
from dash import html
from dash import dcc 
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objs as go
import pandas as pd


app = Dash(__name__)

CARS = pd.read_excel('./assets/AUTO21053A.xlsx')


# # Столбчатые диаграммы
ftb = pd.crosstab(CARS['music'], 'music')
ftb.index.name = 'Категории'
ftb.columns.name = 'music'
# fig.show()
crtx = pd.crosstab(CARS['music'], CARS['signal'], margins=False)

# plotly.express
# Создается графический объект для вывода в браузере
fig1 = px.bar(ftb, x=ftb.index, y="music", color = ftb.index, 
              title='Наличие музыкальной системы')
fig2 = px.bar(crtx, y=crtx.columns, barmode="group", 
              title='Музыкальная система vs Сигнализация')
fig3 = px.scatter(CARS,x=CARS['mlg'], y=CARS['price'], color=CARS['music'])

fig4 = px.box(CARS, x='music', y='price', boxmode='group', notched=True, 
                 points='outliers')

# # С помощью классов
# app.layout = html.Div([
#     html.Div([
#         'LEFT',
#         html.Br(),
#         'LEFT' 
#     ]
#     , id='1', className='test-1')
# ])

# # С помощью id
# app.layout = html.Div([
#     html.Div([
#         'LEFT',
#         html.Br(),
#         'LEFT' 
#     ]
#     , id='t1'),
#     html.Div([
#         'RIGTH',
#         html.Br(),
#         'RIGHT' 
#     ]
#     , id='t2')
# ])

# Графики plotly.express
app.layout = html.Div([
    html.Div([
        dcc.Graph(
            id='music',
            figure=fig1)]
    , id='t1'),
    html.Div([
        dcc.Graph(
            id='music_vs_signal',
            figure=fig2)]
    , id='t2'),
    html.Div([
        dcc.Graph(
            id='price_vs_mlg',
            figure=fig3)]
    , id='t3'),
    html.Div([
        dcc.Graph(
            id='price_vs_music',
            figure=fig4)]
    , id='t4') 
])

if __name__ == '__main__':
    app.run_server(debug=True)

