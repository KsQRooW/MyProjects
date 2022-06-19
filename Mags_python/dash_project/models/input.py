import dash_bootstrap_components as dbc
from dash import html, dcc

dropdown_menu_items_for_input = [
    dbc.DropdownMenuItem("=", id="dropdown-button_sex"),
    dbc.DropdownMenuItem("!=", id="dropdown-button_charges"),
    dbc.DropdownMenuItem(">", id="dropdown-button_smoker"),
    dbc.DropdownMenuItem(">=", id="dropdown-button_region"),
    dbc.DropdownMenuItem("<", id="dropdown-button_age"),
    dbc.DropdownMenuItem("<=", id="dropdown-button_bmi"),
    dbc.DropdownMenuItem("in", id="dropdown-button_children"),
    dbc.DropdownMenuItem("not in", id="dropdown-button_children"),
]

input_style = {
    "width": "10rem",
}

flex_style = {
    "display": "flex"
}

dropdown_param_options = [
    {'label': 'Sex', 'value': 'sex'},
    {'label': 'Smoker', 'value': 'smoker'},
    {'label': 'Region', 'value': 'region'},
    {'label': 'Age', 'value': 'age'},
    {'label': 'BMI', 'value': 'bmi'},
    {'label': 'Charges', 'value': 'charges'},
    {'label': 'Children', 'value': 'children'},
]


class InputParam:
    def __init__(self):
        self._labels_with_criterion = []

    def __call__(self, criterion):
        self._labels_with_criterion.append(self._generate_label(criterion))
        return self

    @staticmethod
    def _generate_label(param: str):
        label = html.Div([
            # dbc.Input(value=param, id=f"view_table_chosen_criterion_{param}", readonly=True,
            #           style=input_style),
            dcc.Dropdown(id=f"view_table_chosen_criterion_{param}", className="dropdown", value=None, options=dropdown_param_options, style=input_style),
            dbc.DropdownMenu(dropdown_menu_items_for_input, id=f"dropdown_menu_for_input_{param}", label="Choose"),
            dbc.Input(style=input_style, id=f"view_table_input_val_{param}"),
            dbc.Button("Delete", id=f"view_table_criterion_delete_{param}", outline=True, color="danger",
                       className="me-1")
        ], style=flex_style)
        return label

    @property
    def labels_with_criterion(self):
        return self._labels_with_criterion

# id="view_table_chosen_criterion"
# id="view_table_input_val_param"
