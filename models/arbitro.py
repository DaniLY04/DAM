# -*- coding: utf-8 -*-

from odoo import models, fields, api

class arbitro(models.Model):
    _name = 'trabajo_final.arbitro'
    _description = 'trabajo_final.arbitro'

    id_arbitro = fields.Integer(string = "id", required = "true")
    nombre = fields.Char(string= "nombre", required = "true")
    deporte = fields.Char(string="Deporte")#fields.One2many("trabajo_final.deporte", string="Deporte", required = "true")
