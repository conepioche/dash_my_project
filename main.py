from dash import Dash
from components import layout

def main():
    app = Dash(__name__)
    app.title = "Les Radars"
    app.layout = [
        layout.create_layout(app)
    ]
    app.run_server()


if __name__ == '__main__':
    main()
