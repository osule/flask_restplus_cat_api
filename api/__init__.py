from flask_restplus import Api

from .namespace1 import ns


api = Api(
    title='My Title',
    version='1.0',
    description='A description',
    # All API metadatas
)

def register_api(app):
    api.add_namespace(ns)
    api.init_app(app)
