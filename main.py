from flask import Flask
from routes.home import home_route
from routes.clientes import cliente_route
####pasta routes, arquivo home e o método home_route###


app = Flask(__name__)

app.register_blueprint(home_route)

app.register_blueprint(cliente_route, url_prefix='/clientes')


app.run(debug=True)  