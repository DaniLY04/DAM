from odoo import models, fields, api


class Team(models.Model):
    _name = 'trabajo_final.team'
    _description = 'Equipo Principal'

    name = fields.Char(string="Nombre", required=True)
    president = fields.Char(string="Presidente" ,required=True)
    country = fields.Char(string="Pais", required=True)
    id_club = fields.Char(string="ID Club", readonly=True, help="El ID del club se asigna automaticamente")
    image = fields.Binary(string="Escudo")

    @api.model
    def create(self, vals):
        if 'id_club' not in vals or not vals['id_club']:
            vals['id_club'] = self.env['ir.sequence'].next_by_code('increment_idclub_sequence')
        return super(Team, self).create(vals)
