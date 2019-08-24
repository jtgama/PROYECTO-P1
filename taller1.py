from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

tipo_medicion = {'sensor': 'TSL561', 'variable':'LUZ solar','unidades': 'lux'}

medicion =[
   {'fecha': '2019-08-23  12:45:07', **tipo_medicion, 'valor': 3000},      
   {'fecha': '2019-08-23  13:05:07', **tipo_medicion, 'valor': 3010},
   {'fecha': '2019-08-23  14:45:07', **tipo_medicion, 'valor': 3050},
   {'fecha': '2019-08-23  17:45:07', **tipo_medicion, 'valor': 3001},
   {'fecha': '2019-08-23  19:45:07', **tipo_medicion, 'valor': 3200},
   {'fecha': '2019-08-23  21:45:07', **tipo_medicion, 'valor': 3400},
   {'fecha': '2019-08-23  20:45:07', **tipo_medicion, 'valor': 3100}
   ]

@app.route("/")
def helloWorld():
  return "Hello word"

@app.route("/")
def get():
  return jsonify(tipo_medicion)

@app.route("/mediciones", methods=["GET"])
def getAll():
      return jsonify(medicion)

@app.route("/mediciones/fecha/<string:date>")
def getByDate(date):
      x = []
      for data in medicion:
            if data["fecha"].find(date) != -1:
                  x.append(data)
      if len(x)==0:
          return "nada"
      return jsonify(x)

@app.route("/mediciones/mediana", methods=["GET"])
def getMed():
      vals = []
      for data in medicion:
          vals.append(data["valor"])
      vals.sort()
      lg = len(vals)
      med = None
      if lg%2 == 0:
        med = str((vals[lg/2] + vals[lg/2+1])/2)
      med = str(vals[int(lg/2)])
      return "La mediana es "+med

@app.route("/mediciones", methods=["POST"])
def postOne():
      now = datetime.now()
      body = request.json
      body["fecha"] = datetime.strftime(now, "%Y-%m-%d %H:%M:%S")
      medicion.append({**body, **tipo_medicion})
      return jsonify(medicion)


app.run(port=5000 ,debug=True)



