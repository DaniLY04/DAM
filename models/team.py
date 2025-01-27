from odoo import models, fields, api, tools


class Team(models.Model):
    _name = 'trabajo_final.team'
    _description = 'Equipo Principal'

    name = fields.Char(string="Nombre : ", required=True)
    president = fields.Char(string="Presidente : " ,required=True)
    country = fields.Char(string="Pais : ", required=True)
    id_club = fields.Char(string="ID Club : ", required=True)
    image = fields.Binary(string="Escudo : ")

    _sql_constraints = [('id_club_unique','UNIQUE(id_club)', 'El ID del club debe ser unico')]

