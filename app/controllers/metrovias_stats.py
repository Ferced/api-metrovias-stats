from flask import Flask, request, jsonify
from flask_restplus import Api, Resource
from server.instance import server
from models.metrovias_stats import Product
from models.metrovias_stats_schema import ProductSchema
from db.database import db,ma


app, api = server.app, server.api

# Init Product Schema
products_schema = ProductSchema(many=True,strict = True)

@api.route('/metrovias_stats')
class MetroviasStats(Resource):
    def get(self):
        #DEVUELVE EL PRODUCTO SEGUN EL ID
        # db.create_all()
        linea=request.json['linea']
        evento=request.json['evento']
        all_products =Product.query.filter_by(linea="#"+linea).filter(Product.tweet.like('%'+evento+'%')).all()
        result = products_schema.dump(all_products)
        return jsonify(result.data)