from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://localhost:27017/Contaminacion'

mongo = PyMongo(app)

@app.route('/GetAll', methods=['GET'])
def get_all_data():
  autos = mongo.db.autos
  output = []
  for s in autos.find():
    output.append({'id' : s['id'],'lat' : s['lat'], 'long' : s['long'], 'vel' : s['vel'], 'ang' : s['ang'], 'fecha' : s['fecha'], 'ign' : s['ign'], 'sat' : s['sat']})
  return jsonify({'result' : output})

@app.route('/GetValue')
def get_one_data():
  latitud = request.args.get('lat', default = 1.0, type = float)
  longitud = request.args.get('long', default = 1.0, type = float)
  autos = mongo.db.autos
  s = autos.find_one({'lat' : latitud,'long':longitud})
  if s:
    output = {'id' : s['id'],'lat' : s['lat'], 'long' : s['long'], 'vel' : s['vel'], 'ang' : s['ang'], 'fecha' : s['fecha'], 'ign' : s['ign'], 'sat' : s['sat']}
  else:
    output = "No se ha encontrado coincidencia"
  return jsonify({'result' : output})

if __name__ == '__main__':
    app.run(debug=True)