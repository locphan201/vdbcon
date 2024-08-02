from flask import Flask
from routes.page_routes import page_blueprint
from routes.api.mysql_routes import mysql_blueprint

app = Flask(__name__)

app.register_blueprint(page_blueprint, url_prefix='/')
app.register_blueprint(mysql_blueprint, url_prefix='/api/mysql')

if __name__ == '__main__':
    app.run(port=8000, debug=True)