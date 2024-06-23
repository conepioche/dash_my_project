from dash import Dash, html, dcc
from . import upload, data_tables, cartographie


def create_layout(app : Dash) -> html.Div:
    return html.Div(className='core-layout',children= [
        html.H1("Les Radars avec Dash"),
        upload.render(app),
        data_tables.render(app),
        cartographie.render(app),
    ])
