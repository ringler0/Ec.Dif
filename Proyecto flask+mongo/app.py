from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/Contaminacion'
mongo = PyMongo(app)

API_KEY="AIzaSyAoPe9_VZO_2EmfopISDb3PKMqqAwmk1mM"
posts = []


def busca(id_auto,latitud,longitud):
  autos = mongo.db.autos
  s = autos.find_one({'id':int(id_auto), 'lat' : str(latitud),'long':str(longitud)})
  if s:
    output = {'id' : s['id'],'lat' : s['lat'], 'long' : s['long'], 'vel' : s['vel'], 'ang' : s['ang'], 'fecha' : s['fecha'], 'ign' : s['ign'], 'sat' : s['sat']}
    b=1
  else:
    output = "No se ha encontrado coincidencia"
    b=0
  return output,b
  #return jsonify({'result' : output})


@app.route("/")
def index():
    return render_template("index.html", num_posts=len(posts))

@app.route("/mostrar", methods=["POST"])
def mapa():
    req = request.form
    id_auto = req['id']
    latitud = str(req['lat'])
    longitud = str(req['long'])
    resultado,b = busca(id_auto,latitud,longitud)
    if b:
      return render_template("mapa.html",id_auto=resultado["id"],latitud=resultado["lat"],longitud=resultado["long"],velocidad=resultado["vel"],angulo=resultado["ang"],fecha=resultado["fecha"],ignicion=resultado["ign"],satelites=resultado["sat"])
    else:
      return resultado

#@app.route('/GetAll', methods=['GET'])
#def get_all_data():
#  autos = mongo.db.autos
#  output = []
#  for s in autos.find():
#    output.append({'id' : s['id'],'lat' : s['lat'], 'long' : s['long'], 'vel' : s['vel'], 'ang' : s['ang'], 'fecha' : s['fecha'], 'ign' : s['ign'], 'sat' : s['sat']})
#  return jsonify({'result' : output})

if __name__ == '__main__':
    app.run(debug=True)