from odoo import models, fields, api

class deporte(models.Model):
    _name = 'trabajo_final.deporte'
    _description = 'trabajo_final.deporte'

    id_deporte = fields.Integer(string = "id", required="true")
    nombre = fields.Char(string="Nombre")
    
    @api.model
    def create(self, vals):
        if 'id_deporte' not in vals or not vals['id_deporte']:
            vals['id_deporte'] = self.env['ir.sequence'].next_by_code('increment_iddeporte_sequence')
        return super(deporte, self).create(vals)