from odoo import models, fields, api

class partido(models.Model):
    _name = 'trabajo_final.partido'
    _description = 'trabajo_final.partido'

    id_partido = fields.Char(string = "id", readonly = True)
    equipo_local = fields.Many2one("trabajo_final.team", string= "equipo local")
    imagen_local = fields.Binary(related="equipo_local.image")
    equipo_visitante = fields.Many2one("trabajo_final.team", string= "equipo visitante")
    imagen_visitante = fields.Binary(related="equipo_visitante.image")
    goles_local = fields.Integer(string = "Goles local", required= "true")
    goles_visitante = fields.Integer(string = "Goles visitante", required= "true")
    estado = fields.Selection([("pendiente", "Pendiente"),
                                ("En curso", "En curso"),
                                ("Finalizado", "Finalizado")], string= "estado", required="true")
    competicion = fields.Many2one("trabajo_final.competicion", string= "competicion", required="true")#fields.Char(string="Competicion")#
    fecha_hora = fields.Datetime(string="Fecha y Hora")
    arbitro_principal = fields.Many2one("trabajo_final.arbitro", string = "Arbitro principal")

    @api.constrains('equipo_local', 'equipo_visitante', 'competicion', 'arbitro_principal')
    def _comprobar_datos(self):
        for record in self:
            if not record.equipo_local:
                raise ValidationError("El campo 'equipo local' es obligatorio.")
            if not record.equipo_visitante:
                raise ValidationError("El campo 'equipo visitante' es obligatorio.")
            if not record.competicion:
                raise ValidationError("El campo 'competición' es obligatorio.")
            if not record.arbitro_principal:
                raise ValidationError("El campo 'árbitro principal' es obligatorio.")

    @api.model
    def create(self, vals):
        if 'id_partido' not in vals or not vals['id_partido']:
            vals['id_partido'] = self.env['ir.sequence'].next_by_code('increment_idpartido_sequence')
        return super(partido, self).create(vals)

    def get_logo_equipoLocal(self):
        if self.equipo_local:
            return self.equipo_local.image
        return False
    
    def get_logo_equipoVisitante(self):
        if self.equipo_visitante:
            return self.equipo_visitante.image
        return False