# -*- coding: utf-8 -*-
"""
dash callbacks

Функции обратного вызова
Новый стиль после upgrade(а)

Таблицы и состояние

pip3 install dash --upgrade

"""

import os
import dash
from dash import Dash, html, dcc, Input, Output, State
from dash import dash_table as tbl
# Не путать с html.Output и dcc.Input
# from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import plotly.express as px
import pandas as pd

# # Демонстрация таблицы
# df = pd.read_excel("./assets/AUTO21053A.xlsx")
#
# app = Dash(__name__)
#
# app.layout = html.Div([
#     html.H1("Вторичный рынок автомобилей"),
#     html.H2("ВАЗ21053"),
#     tbl.DataTable(df.to_dict('records'),
#                   [{"name": i, "id": i} for i in df.columns])
# ], className="table-1")
#
# if __name__ == '__main__':
#     app.run_server(debug=True)

# # Демонстрация таблицы с выбором строк
# df = pd.read_excel("AUTO21053A.xlsx")
#
# app = Dash(__name__)
#
# app.layout = html.Div([
#     html.H1("Вторичный рынок автомобилей"),
#     html.H2("ВАЗ21053"),
#     html.H3("Диапазон возраста"),
#     "От: ",
#     dcc.Input(id='x1', value=str(df['age'].min()),
#               type='number'),
#     "До: ",
#     dcc.Input(id='x2', value=str(df['age'].max()),
#               type='number'),
#     html.H3("Данные автомобилей"),
#     tbl.DataTable(df.to_dict('records'),
#                   [{"name": i, "id": i} for i in df.columns],
#                   style_cell={'padding': '5px',
#                               'textAlign': 'center'},
#                   style_header={
#                                 'backgroundColor': 'blue',
#                                 'color': 'yellow',
#                                 'fontWeight': 'bold'},
#                   id='df')
# ], className="table-1")
#
# @app.callback(
#     Output('df', 'data'),
#     Input('x1', 'value'),
#     Input('x2', 'value'))
# def update_figure(x1, x2):
#     sel = (df['age'] >= int(x1)) & (df['age'] <= int(x2))
#     table = df[sel].to_dict('records')
#     return table
#
# if __name__ == '__main__':
#     app.run_server(debug=True)

#--------------------------------------------------------------------

# Вывод таблицы кусочками

app = Dash(__name__)

df = pd.read_excel("./assets/AUTO21053A.xlsx")

PAGE_SIZE = 10

app.layout = tbl.DataTable(
    id='datatable-paging',
    columns=[
        {"name": i, "id": i} for i in sorted(df.columns)
    ],
    page_current=0,
    page_size=PAGE_SIZE,
    page_action='custom'
)


@app.callback(
    Output('datatable-paging', 'data'),
    Input('datatable-paging', "page_current"),
    Input('datatable-paging', "page_size"))
def update_table(page_current, page_size):
    return df.iloc[
        page_current * page_size:(page_current + 1)*page_size
    ].to_dict('records')


if __name__ == '__main__':
    app.run_server(debug=True)

#--------------------------------------------------------------------

# # Сохранение состояния - выбора бользователя - без callback
# # Поступление значения Input вызывает callback.
# # State - хранит значение до изменения
# app = dash.Dash(__name__)
#
# app.layout = html.Div([
#     dcc.Input(id='input-1-state', type='text', value='Питер'),
#     dcc.Input(id='input-2-state', type='text', value='Москва'),
#     html.Button(id='submit-button-state', n_clicks=0, children='Submit'),
#     html.Div(id='output-state')
# ])
# @app.callback(Output('output-state', 'children'),
#               [Input('submit-button-state', 'n_clicks')],
#               [State('input-1-state', 'value'),
#                State('input-2-state', 'value')])
# def update_output(n_clicks, input1, input2):
#     return u'''
#         Кнопка была нажата {} раз,
#         Input 1 - это "{}",
#         и Input 2 - это "{}"
#     '''.format(n_clicks, input1, input2)

#
# if __name__ == '__main__':
#     app.run_server(debug=True)
