from flask import render_template

from flask import Flask, jsonify, request

from flask_sqlalchemy import SQLAlchemy

import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property

from flask_restplus import Api


import psycopg2

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost:5433/flasktest_db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

"""
_________________________
    HACIENDO UN RESTFULL API SERVER 
_________________________
"""

api_v1 = Api(
    version='1.0',
    title="FLASK | FLASK-RESTPlus GeoAPI",
    description=(
        "This is a FLASK-RESPlus powered API with geospatial super power.\n\n"
        "Checkout more at https://gis-ops.com or https://github.com/gis-ops\n"
    ),
)
api_v1.init_app(app)

import geopy.distance
import pyproj
#from app.modules.geoapi import GeoApiNamespace
from flask import request
from flask_restplus import Namespace, Resource, abort
from flask_restplus import fields
from functools import partial
from geopy import Point as GeopyPoint, distance
from http import HTTPStatus
from shapely.geometry import Polygon, LineString
from shapely.ops import transform

from geoalchemy2 import Geometry

api = Namespace('geoapi', description="GeoApiNamespace.description")


















db = SQLAlchemy(app)

class Persona(db.Model):
    ci = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), unique=True)
    apellido = db.Column(db.String(80), unique=True)

class Uma_table(db.Model):
    register_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    time = db.Column(db.String(8))
    uma = db.Column(db.Integer)
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    mp01 = db.Column(db.Integer)
    mp25 = db.Column(db.Integer)
    mp10 = db.Column(db.Integer)
    d03 = db.Column(db.Integer)
    d05 = db.Column(db.Integer)
    d01 = db.Column(db.Integer)
    d25 = db.Column(db.Integer)
    d50 = db.Column(db.Integer)
    d10 = db.Column(db.Integer)
    vel = db.Column(db.Float)
    geo = db.Column(Geometry(geometry_type="POINT"))
 
@app.route('/api/v1.0/mensaje')
def create_task():
    var1 = request.args.get('var1')
    response = jsonify(var1)
    #response = jsonify('Hola mundo desde Flask')
    response.headers.add("Access-Control-Allow-Origin", "*")
    

    return response


@app.route('/point/distance/')
#@app.param('start_lat', 'Latitude of the start point e.g. 52.52624809700062', _in="query")
#@app.param('start_lng', 'Longitude of the start point e.g. 13.4197998046875', _in="query")
#@app.param('end_lat', 'Latitude of the end point e.g. 52.50535544522142', _in="query")
#@app.param('end_lng', 'Longitude of the end point e.g. 13.366928100585938', _in="query")
#"""Return the distance in kilometers between two points."""
#@app.doc(id='point_to_point_distance')
def get_distance():
    """
    Return the distance in kilometers between two points.
    """

    if request.args.get('start_lat', '') and request.args.get('start_lng', '') and request.args.get('end_lat', '') and request.args.get('end_lng', ''):
        try:
            response = jsonify(geopy.distance.distance(
                GeopyPoint(
                    longitude=request.args.get('start_lng', type=float),
                    latitude=request.args.get('start_lat', type=float)
                ),
                GeopyPoint(
                    longitude=request.args.get('end_lng', type=float),
                    latitude=request.args.get('end_lat', type=float)
                )
                ).km
            )
                
            response.headers.add("Access-Control-Allow-Origin", "*")
            return response
    
        except Exception:
            return jsonify("error alguno").headers.add("Access-Control-Allow-Origin", "*")

        abort(HTTPStatus.BAD_REQUEST,
                message="Please provide a valid query e.g. with the following url arguments: "
                        "http://127.0.0.1:5000/api/geoapi/point/distance/?start_lng=8.83546&start_lat=53.071124&end_lng=10.006168&end_lat=53.549926")
    
if __name__ == '__main__':
    app.run(debug=True)