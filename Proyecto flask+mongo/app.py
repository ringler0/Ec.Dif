from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb+srv://nico:noentiendoalprofe@cluster0.7ran0.mongodb.net/Contaminacion'

mongo = PyMongo(app)

@app.route('/GetAll', methods=['GET'])
def get_all_data():
  Data = mongo.db.Data
  output = []
  for s in Data.find():
    output.append({'time' : s['time'],'uma' : s['uma'], 'lat' : s['lat'], 'lon' : s['lon'], 'mp01' : s['mp01'], 'mp25' : s['mp25'], 'mp10' : s['mp10'], 'd03' : s['d03'], 'd05' : s['d05'], 'd01' : s['d01'], 'd25' : s['d25'], 'd50' : s['d50'], 'd10' : s['d10'], 'vel' : s['vel']})
  return jsonify({'result' : output})

@app.route('/GetValue')
def get_one_data():
  latitud = request.args.get('lat', default = 1.0, type = float)
  longitud = request.args.get('long', default = 1.0, type = float)
  Data = mongo.db.Data
  s = Data.find_one({'lat' : latitud,'lon':longitud})
  if s:
    output = {'time' : s['time'],'uma' : s['uma'], 'lat' : s['lat'], 'lon' : s['lon'], 'mp01' : s['mp01'], 'mp25' : s['mp25'], 'mp10' : s['mp10'], 'd03' : s['d03'], 'd05' : s['d05'], 'd01' : s['d01'], 'd25' : s['d25'], 'd50' : s['d50'], 'd10' : s['d10'], 'vel' : s['vel']}
  else:
    output = "No se ha encontrado coincidencia"
  return jsonify({'result' : output})

if __name__ == '__main__':
    app.run(debug=True)