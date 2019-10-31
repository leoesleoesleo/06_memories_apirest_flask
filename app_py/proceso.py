# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 21:30:32 2019

@author: leonardo.patino
"""

class ServicioApi:
    
    def inicializar(self,fechaini,fechafin):
        self.fechaini = fechaini
        self.fechafin = fechafin
    
    def proceso(self):
        c = self.fechaini, self.fechafin
        return c
"""        
proceso_api = ServicioApi()
proceso_api.inicializar('2019-07-10','2019-07-15')
res = proceso_api.proceso()
"""      
        