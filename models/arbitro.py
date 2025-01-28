# -*- coding: utf-8 -*-

from odoo import models, fields, api

class arbitro(models.Model):
    _name = 'trabajo_final.arbitro'
    _description = 'trabajo_final.arbitro'

    id_arbitro = fields.Integer(string = "id", required = "true")
    nombre = fields.Char(string= "nombre", required = "true")
    deporte = fields.Many2one("trabajo_final.deporte", string="Deporte", required = "true")
    
    _sql_contraints = [
        ("deporte_uk", "UNIQUE(deporte)", "Un arbitro solo puede estas asociado a un deporte")
        ("nombre_uk", "UNIQUE(nombre)", "No puede haber arbitros con el mismo nombre")
    ]
