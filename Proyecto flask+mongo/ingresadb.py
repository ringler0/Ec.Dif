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

cont=1
for row in aReader:
    cont+=1
    dic={"id":int(row[0]),"lat":float(row[1]),"long":float(row[2]),"vel":int(row[3]),"ang":int(row[4]),"fecha":row[5],"ign":int(row[6]),"sat":int(row[7])}
    dic_json=json.dumps(dic, indent=4, ensure_ascii=False)
    dato=json.loads(dic_json)
    autos.insert_one(dato)
    print(cont)