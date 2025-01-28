from odoo import models, fields


class Team(models.Model):
    _name = 'trabajo_final.team'
    _description = 'Equipo Principal'

    name = fields.Char(string="Nombre : ", required=True)
    president = fields.Char(string="Presidente : " ,required=True)
    country = fields.Char(string="Pais : ", required=True)
    id_club = fields.Char(string="ID_Club", default=lambda self: self.env['ir.sequence'].next_by_code('increment_idclub_sequence'))
    image = fields.Binary(string="Escudo : ")
