from odoo import models, fields, api

class competicion(models.Model):
    _name = 'trabajo_final.competicion'
    _description = 'trabajo_final.competicion'

    id_competicion = fields.Char(string = "id", readonly = True)
    name = fields.Char(string="Nombre")
    pais = fields.Char(string="Pais")
    deporte = fields.Char(string="Deporte")#fields.Many2one("trabajo_final.deporte", string="Deportes", required="true")
    categoria = fields.Char(string="Categoria")#fields.Many2one("trabajo_final.categoria", string="Categoria", required="true")
    listado_de_equipos = fields.Char(string="Equipos")#fields.Many2one("trabajo_final.equipo", string="Equipos", required="true")

    @api.model
    def create(self, vals):
        if 'id_competicion' not in vals or not vals['id_competicion']:
            vals['id_competicion'] = self.env['ir.sequence'].next_by_code('increment_idcompeticion_sequence')
        return super(competicion, self).create(vals)