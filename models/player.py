from odoo import models, fields, api


class Player(models.Model):
    _name = 'trabajo_final.player'
    _description = 'Jugadores'

    name = fields.Char(string="Nombre", required = True)
    id_player = fields.Char(string="ID_Jugador", readonly=True)
    last_name = fields.Char(string ="Apellidos", requiered = True)

    gender = fields.Selection([
        ('first','Masculino'),
        ('second','Femenino')
    ], string="Genero", required = True)

    image = fields.Binary(string="Foto")

    team_sport_division_id = fields.Many2one('trabajo_final.team_sport_division',string="Equipo")
    status_id = fields.Many2many('trabajo_final.status',string="Estado")
    position_id = fields.Many2one('trabajo_final.position',string="Posicion", ondelete="set null")
    division_name = fields.Char(related="team_sport_division_id.name")
    status_name = fields.Char(related="status_id.name")    
    position_name = fields.Char(related="position_id.name")

    @api.model
    def create(self, vals):
        if 'id_player' not in vals or not vals['id_player']:
            vals['id_player'] = self.env['ir.sequence'].next_by_code('increment_idplayer_sequence')
        return super(Player, self).create(vals)
    
    @api.onchange('team_sport_division_id')
    def _onchange_team_id(self):
        if self.team_sport_division_id and self.team_sport_division_id.name == 'Sin Equipo':
            return {
                'domain': {
                    'status_id': [('name', 'like', ['Jubilado', 'Libre','Lesionado','Dudoso'])]
                }
            }
        else:
            return {
                'domain': {
                    'status_id': []
                }
            }