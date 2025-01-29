from odoo import models, fields


class Team(models.Model):
    _name = 'trabajo_final.team'
    _description = 'Equipo Principal'

    name = fields.Char(string="Nombre", required=True)
    president = fields.Char(string="Presidente" ,required=True)
    country = fields.Char(string="Pais", required=True)
    id_club = fields.Char(string="ID Club", readonly=True, help="El ID del club se asigna automaticamente")
    image = fields.Binary(string="Escudo")
