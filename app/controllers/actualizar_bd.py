from flask import Flask, request, jsonify
from flask_restplus import Api, Resource
from server.instance import server
from models.metrovias_stats import Product
from models.metrovias_stats_schema import ProductSchema
from db.database import db,ma
from helpers.actualizarTweets import ActualizarTweets


app, api = server.app, server.api

# Init Product Schema
product_schema = ProductSchema(strict = True)

@api.route('/metrovias_stats_actualizar')
class MetroviasStats(Resource):
    def get(self):
        todo_los_tweets=ActualizarTweets.get_all_tweets("Metrovias")
        for tweet in todo_los_tweets:
            new_product = Product(ActualizarTweets.nombreLinea(tweet[1]),tweet[1],tweet[0])
            db.session.add(new_product)
        db.session.commit()
        return product_schema.jsonify("ok")
