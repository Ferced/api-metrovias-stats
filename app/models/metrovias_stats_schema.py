from flask_marshmallow import Marshmallow
ma=Marshmallow()
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id','linea','tweet','fecha')