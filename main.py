from dash import Dash
from components import layout

app = Dash(__name__)
server = app.server
app.title = "Les Radars"
app.layout = [layout.create_layout(app)]



if __name__ == '__main__':
    app.run()
