from odoo import models, fields, api

class Position(models.Model):
    _name = 'trabajo_final.position'
    _description = 'Posicion del Jugador'

    name = fields.Char(string="Nombre")
    id_position = fields.Char(string="ID Posicion", readonly=True, help="El ID de la posicion se asigna automaticamente")

    @api.model
    def create(self, vals):
        if 'id_position' not in vals or not vals['id_position']:
            vals['id_position'] = self.env['ir.sequence'].next_by_code('increment_idposition_sequence')
        return super(Position, self).create(vals)

