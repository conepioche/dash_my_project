from dash import Dash,html, dcc
from . import ids

def render(app : Dash) -> html.Div:
    return html.Div(children= dcc.Upload('Selectionner un fichier',id = ids.UPLOADER ))