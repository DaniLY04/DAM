from odoo import models, fields, api

class Trainer(models.Model):
    _name = 'trabajo_final.trainer'
    _description = 'Entrenador'

    name = fields.Char(string="Nombre",required=True)
    last_name = fields.Char(string="Apellidos",required=True)
    age = fields.Integer(string="Edad")
    id_trainer = fields.Char(string="ID",readonly=True)
    id_team = fields.Many2one('trabajo_final.team',string="Equipo",required=True)
    
    @api.model
    def create(self, vals):
        if 'id_trainer' not in vals or not vals['id_trainer']:
            vals['id_trainer'] = self.env['ir.sequence'].next_by_code('increment_idTrainer_sequence')
        return super(Trainer, self).create(vals)