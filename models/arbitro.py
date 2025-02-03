# -*- coding: utf-8 -*-

from odoo import models, fields, api

class arbitro(models.Model):
    _name = 'trabajo_final.arbitro'
    _description = 'trabajo_final.arbitro'

    id_arbitro = fields.Char(string = "id", readonly = True)
    nombre = fields.Char(string= "nombre", required = "true")
    deporte = fields.Many2one("trabajo_final.deporte", string="Deporte", required = "true")
   
    @api.model
    def create(self, vals):
        if 'id_arbitro' not in vals or not vals['id_arbitro']:
            vals['id_arbitro'] = self.env['ir.sequence'].next_by_code('increment_idarbitro_sequence')
        return super(arbitro, self).create(vals)