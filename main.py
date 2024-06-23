from dash import Dash
from flask import Flask
from components import layout
server = Flask(__name__)
def main():
    app = Dash(__name__,server)
    app.title = "Les Radars"
    app.layout = [
        layout.create_layout(app)
    ]
    app.run_server()


if __name__ == '__main__':
    main()
