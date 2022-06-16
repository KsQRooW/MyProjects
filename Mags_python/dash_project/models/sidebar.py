from dash import dcc, html
import dash_bootstrap_components as dbc

SIDESTYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#222222",
}

CONTSTYLE = {
    "margin-left": "18rem",
    "margin-right": "3rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div([
    dcc.Location(id="url"),
    html.Div(
        [
            html.H6("Analyze", className="display-3", style={'color': 'white'}),
            html.Hr(style={'color': 'white'}),
            dbc.Nav(
                [
                    dbc.NavLink("Analysis", href="/page1", active="exact"),
                    dbc.NavLink("The effect", href="/page2", active="exact"),
                    dbc.NavLink("Thanks", href="/page3", active="exact"),
                    dbc.NavLink("Histograms", href="/page4", active="exact"),
                ],
                vertical=True, pills=True),
        ],
        style=SIDESTYLE
    ),
    html.Div(id="page-content", children=[], style=CONTSTYLE)
])
