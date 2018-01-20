from demo.setup import app
from api import register_api

register_api(app)

if __name__ == '__main__':
     app.run()

# https://flask-restplus.readthedocs.io/en/stable/scaling.html