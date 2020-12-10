import csv,json
import pymongo


conexion = pymongo.MongoClient("localhost",27017)
db = conexion["Contaminacion"]
autos = db["autos"]
"""
1: id del vehículo, 
2: latitud (GPS),
3: longitud (GPS),
4: velocidad
5: ángulo de movimiento,
6: fecha (día, hora, minutos, segundos)
7: ignición (vehículo encendido o no) 
8: número de satélites
"""

fData=open('./particion.csv','r', encoding='utf-8')
aReader=csv.reader(fData)


for row in aReader:
    dic={"id":row[0],"lat":row[1],"long":row[2],"vel":row[3],"ang":row[4],"fecha":row[5],"ign":row[6],"sat":row[7]}
    dic_json=json.dumps(dic, indent=4, ensure_ascii=False)
    dato=json.loads(dic_json)
    #print (dato["id"])
    autos.insert_one(dato)