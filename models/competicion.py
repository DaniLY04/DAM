from odoo import models, fields, api
from odoo.exceptions import ValidationError

class competicion(models.Model):
    _name = 'trabajo_final.competicion'
    _description = 'trabajo_final.competicion'

    id_competicion = fields.Char(string = "id", readonly = True)
    name = fields.Char(string="Nombre")
    pais = fields.Char(string="Pais")
    deporte = fields.Many2one("trabajo_final.deporte", string="Deporte", required="true")
    categoria = fields.One2one("trabajo_final.categoria", string="Categoria", required="true")
    listado_de_equipos = fields.Many2many("trabajo_final.team_sport_division", string="Equipos", ondelete="cascade", required="true")

    @api.model
    def create(self, vals):
        if 'id_competicion' not in vals or not vals['id_competicion']:
            vals['id_competicion'] = self.env['ir.sequence'].next_by_code('increment_idcompeticion_sequence')
        return super(competicion, self).create(vals)

    @api.constrains('listado_de_equipos')
    def _check_equipos_competicion(self):
        for record in self:
            if len(record.listado_de_equipos) < 2:
                raise ValidationError("Una competición debe tener al menos dos equipos.")
            equipos_ids = [equipo.id for equipo in record.listado_de_equipos]
            if len(equipos_ids) != len(set(equipos_ids)):
                raise ValidationError("No puede haber equipos duplicados en la competición.")
