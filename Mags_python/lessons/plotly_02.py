# -*- coding: utf-8 -*-
"""
Изучение Plotly DASH
Run this app with `python app.py` and
visit http://127.0.0.1:8050/ in your web browser.
"""
import os
os.chdir("d:/work.p/")
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

CARS = pd.read_excel('./data/AUTO21053A.xlsx')

# # Столбчатые диаграммы
ftb = pd.crosstab(CARS['music'], 'music')
ftb.index.name = 'Категории'
ftb.columns.name = 'music'
fig1 = px.bar(ftb, x=ftb.index, y="music", color = ftb.index)
# fig.show()
crtx = pd.crosstab(CARS['music'], CARS['signal'], margins=False)
# Создается графический объект для вывода в браузере
fig2 = px.bar(crtx, y=crtx.columns, barmode="group")
# fig.show()

colors = {
    'background': '#00AA00',
    'text': '#7FDBFF'
}

app.layout = html.Div(children=[
html.H1('Графический анализ данных', 
        style={'textAlign': 'center', 'color':colors['text']}),
html.Div('Вторичный рынок автомобилей', className='theme-1'),
html.Img(src='/assets/авто.jpg',
         style={'margin-left': '80%','height':'10%', 'width':'10%'}),
html.Div([
dcc.Graph(
    id='music',
    figure=fig1, style={'height':'15%', 'width':'25%', 'margin-left': '10%', 'margin-top': '5%'}), 
dcc.Graph(
    id='music_vs_signal',
    figure=fig2, style={'height':'15%', 'width':'25%', 'margin-left': '30%', 'margin-top': '5%' })
])
], id = 'main', style={'backgroundColor': colors['background']})

if __name__ == '__main__':
    app.run_server(debug=True)

