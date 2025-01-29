from odoo import models, fields, api

class partido(models.Model):
    _name = 'trabajo_final.partido'
    _description = 'trabajo_final.partido'

    id_partido = fields.Char(string = "id", default=lambda self: self.env['ir.sequence'].next_by_code('increment_idpartido_sequence'), readonly = True)
    equipo_local = fields.Many2one("trabajo_final.team", string= "equipo local", required = "true")
    equipo_visitante = fields.Many2one("trabajo_final.equipo", string= "equipo visitante", required = "true")
    goles_local = fields.Integer(string = "Goles local", required= "true")
    goles_visitante = fields.Integer(string = "Goles visitante", required= "true")
    estado = fields.Selection([("pendiente", "Pendiente"),
                                ("En curso", "En curso"),
                                ("Finalizado", "Finalizado")], string= "estado", required="true")
    competicion = fields.Many2one("trabajo_final.competicion", string= "competicion", required="true")#fields.Char(string="Competicion")#
    fecha_hora = fields.Datetime(string="Fecha y Hora")
    arbitro_principal = fields.Many2one("trabajo_final.arbitro", string = "Arbitro principal", required="true")

