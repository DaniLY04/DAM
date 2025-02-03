from odoo import models, fields, api


class Division(models.Model):
    _name = 'trabajo_final.division'
    _description = 'Categoria'

    name = fields.Char(string="Nombre : ", requiered=True)
    id_division = fields.Char(string="ID :" , required=True)

    @api.model
    def create(self, vals):
        if 'id_division' not in vals or not vals['id_division']:
            vals['id_division'] = self.env['ir.sequence'].next_by_code('increment_idDivision_sequence')
        return super(Division, self).create(vals)