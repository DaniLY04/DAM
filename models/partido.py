from odoo import models, fields, api

class partido(models.Model):
    _name = 'trabajo_final.partido'
    _description = 'trabajo_final.partido'

    id_partido = fields.Integer(string = "id", required="true")
    equipo_local = fields.Char(string="Equipo local")#fields.Char("trabajo_final.equipo", string= "equipo_local", required = "true")
    equipo_visitante = fields.Char(string="Equipo visitante")#fields.Char("trabajo_final.equipo", string= "equipo_local", required = "true")
    goles_local = fields.Integer(string = "Goles local", required= "true")
    goles_visitante = fields.Integer(string = "Goles visitante", required= "true")
    estado = fields.Char(string= "estado", required="true")
    competicion = fields.Char(string="Competicion")#fields.One2many("trabajo_final.competicion", string= "competicion", required="true")
    fecha_hora = fields.Datetime(string="Fecha y Hora")
    arbitro_principal = fields.Many2one("trabajo_final.arbitro", string = "Arbitro principal", required="true")