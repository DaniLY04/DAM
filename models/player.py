from odoo import models, fields


class Player(models.Model):
    _name = 'trabajo_final.player'
    _description = 'Jugadores'

    name = fields.Char(string="Nombre", required = True)
    id_player = fields.Char(string="ID_Jugador", default=lambda self: self.env['ir.sequence'].next_by_code('increment_idplayer_sequence'), readonly=True)
    last_name = fields.Char(string ="Apellidos", requiered = True)

    gender = fields.Selection([
        ('first','Masculino'),
        ('second','Femenino')
    ], string="Genero", required = True)

    image = fields.Binary(string="Foto")