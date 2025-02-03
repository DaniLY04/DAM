from odoo import models, fields, api


class Team_Sport_Division(models.Model):
    _name = 'trabajo_final.team_sport_division'
    _description = 'Equipos Deporte Categoria'

    name = fields.Char(string="Nombre", required = True)
    id = fields.Char(string="ID", readonly=True)
    id_sport = fields.Many2one('trabajo_final.deporte',string="Deporte")
    id_team = fields.Many2one('trabajo_final.tem',string="Equipo Padre")
    id_division = fields.Many2one('trabajo_final.division', string="Categoria")
    id_trainer = fields.Many2one('trabajo_final.trainer',string="Entrenador")
    jugadores = fields.One2Many('trabajo_final.player',string="Jugadores")

    @api.model
    def create(self, vals):
        if 'id' not in vals or not vals['id']:
            vals['id'] = self.env['ir.sequence'].next_by_code('increment_idTDS_sequence')
        return super(Team_Sport_Division, self).create(vals)