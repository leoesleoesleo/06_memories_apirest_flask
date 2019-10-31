# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 21:19:37 2019

@author: leonardo.patino
"""

from flask import Flask
from flask_restful import Resource, Api
import proceso

app = Flask(__name__)
api = Api(app)

class Api(Resource):
    
    def get(self,fechaini,fechafin):
        
        proceso_api = proceso.ServicioApi()
        proceso_api.inicializar(fechaini,fechafin)
        res = proceso_api.proceso()
        
        json = [{"fechaini":res[0]},
                {"fechafin":res[1]}
                ]
        return json
        
api.add_resource(Api, '/fechaini/<fechaini>/fechafin/<fechafin>')

if __name__ == '__main__':
    app.run(debug=True)
    
    
#http://localhost:5000/fechaini/2019-07-10/fechafin/2019-07-15    
    