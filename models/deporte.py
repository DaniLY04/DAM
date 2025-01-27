from odoo import models, fields, api

class deporte(models.Model):
    _name = 'trabajo_final.deporte'
    _description = 'trabajo_final.deporte'

    id_deporte = fields.Integer(string = "id", required="true")
    nombre = fields.Char(string="Nombre")