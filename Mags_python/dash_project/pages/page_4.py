from dash import dcc, html

graf = {
    "padding-left": "4rem",
    "display": "inline-block"
}

page_4 = [
    html.Div(
        children=[
            html.H1('Histograms', className='header-title',
                    style={'textAlign': 'center'})
        ], className='header'),

    dcc.Dropdown(
        id='page4_drop',
        options=[
            {'label': 'Histogram', 'value': 'Histogram'},
            {'label': 'Distplot', 'value': 'Distplot'},
        ],
        value='Histogram', className="dropdown", style={'margit-bottom': '32px'}
    ),

    html.Div([
        dcc.Graph(id='graph_4_1', className="card", style=graf),
        dcc.Graph(id='graph_4_2', className="card", style=graf),
    ]),

    html.Div([
        dcc.Graph(id='graph_4_3', className="card", style=graf),
        dcc.Graph(id='graph_4_4', className="card", style=graf),
    ])
    # dcc.Graph(id='graph2',
    #           figure=px.scatter(df, x='age',
    #                             y='charges', facet_col='smoker'), className="card")
]
