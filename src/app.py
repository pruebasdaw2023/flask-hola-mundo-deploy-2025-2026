from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():

    username = os.getenv('MI_USERNAME')
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')

    print(username, email, password)

    return '<h1>Mi primera aplicacion Flask deployeada en Render.<br><br>{}<br>{}<br>{}<br></h1>'.format(username, email, password), 200


@app.route('/healthz')
def healthz():
    return 'OK', 200


def status_404(error):
    return '<h1>404 Not Found</h1>'

app.register_error_handler(404, status_404)

if __name__ == '__main__':

    app.run(debug=True)