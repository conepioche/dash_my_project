from dash import Dash, html, dcc
from dash.dependencies import Output,Input, State
import pandas as pd
import plotly.express as px
from . import ids
from .data_tables import DataSchema


def render(app : Dash) -> html.Div:
    @app.callback(
        Output(ids.MAP,'children'),
        Input(ids.SHOW_MAP,"n_clicks"),
        State(ids.TABLE,"data"),
    )
    def map(n_clicks : int,data : dict) -> dcc.Graph:
        if n_clicks == 0:
            pass
        else:
            df = pd.DataFrame(data)
            px.set_mapbox_access_token("pk.eyJ1IjoiY29uZXBpb2NoZSIsImEiOiJjbG1nOTVwNTkyZ3ZiM3BvNXJ6d2tlb2U1In0.9uCd1V5Duow2kbsBtn6N-g")
            fig = px.scatter_mapbox(df,lat=DataSchema.LATITUDE,lon = DataSchema.LONGITUDE,color=DataSchema.DEPARTEMENT,zoom= 4)
            return dcc.Graph(figure= fig)   

    return html.Div(id = ids.MAP)