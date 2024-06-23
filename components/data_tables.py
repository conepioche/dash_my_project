from dash import Dash, html, dcc, dash_table
from dash.dependencies import Output, Input, State
from dataclasses import dataclass
import pandas as pd
import io
import base64
from . import ids

@dataclass
class DataSchema:
    LATITUDE ="latitude"
    LONGITUDE = "longitude"
    DEPARTEMENT = "departement"
    VITESSE = "vitesse_vehicules_legers_kmh"


def render(app : Dash) -> html.Div:
    @app.callback(
    Output(ids.FILENAME,"children"),
    Output(ids.TABLE,"data"),
    Output(ids.BUTTON,"children"),
    Input(ids.UPLOADER,"contents"),
    State(ids.UPLOADER,"filename"),
    )
    def load_file(contents : list,filename : str)-> list[str,dict,html.Button]:
        if contents is not None:
            contents_type , contents_string = contents.split(',')
            decoded = base64.b64decode(contents_string)
            df = pd.read_csv(io.StringIO(decoded.decode('utf-8')),sep = ',')
            df_modified = df[df.type == "Radar fixe"][[DataSchema.DEPARTEMENT,DataSchema.LATITUDE,DataSchema.LONGITUDE,DataSchema.VITESSE]]
            return f'Vous avez ouvert le fichier {filename}', df_modified.to_dict('records'),html.Button('Afficher la carte',n_clicks=0,id = ids.SHOW_MAP)
    return html.Div(className = 'carte',
        children = [
            html.H2(id=ids.FILENAME),

            dash_table.DataTable(
            id = ids.TABLE,
            page_size=10),
            html.Div(id = ids.BUTTON)
            ])