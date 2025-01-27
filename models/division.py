from odoo import models, fields, api


class Division(models.Model):
    _name = 'trabajo_final.division'
    _description = 'Categoria'

    name = fields.Char(string="Nombre : ", requiered=True)
    id_division = fields.Integer(string="ID :" , required=True)

    _sql_constraints = [('id_division_unique'),('UNIQUE(id_division)'),('El ID debe ser unico')]