from dash import Dash
from components import layout

app = Dash(__name__)
server = app.server
          
def main():
    app.title = "Les Radars"
    app.layout = [
        layout.create_layout(app)
    ]
    app.run()


if __name__ == '__main__':
    main()
