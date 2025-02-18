from odoo import models, fields, api


class Division(models.Model):
    _name = 'trabajo_final.division'
    _description = 'Categoria'

    name = fields.Char(string="Nombre : ", required=True)
    id_division = fields.Char(string="ID :")
    gender = fields.Selection([
        ('first','Masculino'),
        ('second','Femenino')
    ], string="Genero", required = True)
    id_sport = fields.Many2one("trabajo_final.deporte", string="Deporte")
    
    @api.model
    def create(self, vals):
        if 'id_division' not in vals or not vals['id_division']:
            vals['id_division'] = self.env['ir.sequence'].next_by_code('increment_idDivision_sequence')
        return super(Division, self).create(vals)