from dash import dcc, html
import plotly.express as px

from Mags_python.dash_project.settings import df

page_2 = [
    html.Div(
        children=[
            html.H1('The effect of the carat on price', className='header-title',
                    style={'textAlign': 'center'})
        ], className='header'),
    dcc.Graph(id='graph_2_1',
              figure=px.scatter(df, x='age',
                                y='charges'), className="card"),

    dcc.Graph(id='graph_2_2',
              figure=px.scatter(df, x='age',
                                y='charges', facet_col='smoker'), className="card")
]
