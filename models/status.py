# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Status(models.Model):
    _name = 'trabajo_final.status'
    _description = 'Estado del Jugador'

    name = fields.Char(string="Nombre")
    id_status = fields.Char(string="ID Estatus", readonly=True, help="El ID del estatus se asigna automaticamente")

    @api.model
    def create(self, vals):
        if 'id_status' not in vals or not vals['id_status']:
            vals['id_status'] = self.env['ir.sequence'].next_by_code('increment_idstatus_sequence')
        return super(Status, self).create(vals)
