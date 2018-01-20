from flask_restplus import Namespace, Resource, fields

from demo import db

ns = Namespace('cats', description='Cats related operations')

cat = ns.model('Cat', {
    'id': fields.String(required=True, description='The cat identifier'),
    'name': fields.String(required=True, description='The cat name'),
})

CATS = [
    {'id': 'felix', 'name': 'Felix'},
]



@ns.route('/')
class CatList(Resource):
    @ns.doc('list_cats')
    @ns.marshal_list_with(cat)
    def get(self):
        '''List all cats'''
        print(db)
        return CATS
