from odoo import models, fields, api

class competicion(models.Model):
    _name = 'trabajo_final.competicion'
    _description = 'trabajo_final.competicion'

    id_competicion = fields.Integer(string = "id", required="true")
    nombre = fields.Char(string="Nombre")
    pais = fields.Char(string="Pais")
    deporte = fields.Char(string="Deporte")#fields.Many2one("trabajo_final.deporte", string="Deportes", required="true")
    categoria = fields.Char(string="Categoria")#fields.Many2one("trabajo_final.categoria", string="Categoria", required="true")
    listado_de_equipos = fields.Char(string="Equipos")#fields.Many2one("trabajo_final.equipo", string="Equipos", required="true")