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

    team_id = fields.Many2one('trabajo_final.team',string="Equipo")
    status_id = fields.Many2many('trabajo_final.status',string="Estado")
    position_id = fields.Many2one('trabajo_final.position',string="Posicion", ondelete="set null")

    @api.model
    def create(self, vals):
        if 'id_player' not in vals or not vals['id_player']:
            vals['id_player'] = self.env['ir.sequence'].next_by_code('increment_idplayer_sequence')
        return super(Player, self).create(vals)
    
    @api.onchange('team_id')
    def _onchange_team_id(self):
        if self.team_id and self.team_id.name == 'Sin Equipo':
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