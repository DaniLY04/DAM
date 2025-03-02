from odoo import models, fields, api
from odoo.exceptions import ValidationError

from datetime import timedelta

class partido(models.Model):
    _name = 'trabajo_final.partido'
    _description = 'trabajo_final.partido'

    id_partido = fields.Char(string = "Id", readonly = True)
    equipo_local = fields.Many2one("trabajo_final.team_sport_division", string= "Equipo local")
    imagen_local = fields.Binary(related="equipo_local.id_team.image")
    equipo_visitante = fields.Many2one("trabajo_final.team_sport_division", string= "Equipo visitante")
    imagen_visitante = fields.Binary(related="equipo_visitante.id_team.image")
    resultado = fields.Char(string = "Resultado", required= True)
    estado = fields.Char(string = "Estado", readonly = True, compute = "_actualizar_estado")
    competicion = fields.Many2one("trabajo_final.competicion", string= "Competicion", required= True)
    fecha_hora = fields.Datetime(string="Fecha y Hora")
    arbitro_principal = fields.Many2one("trabajo_final.arbitro", string = "Arbitro principal", required = True)
    #campo xpath
    comentario = fields.Text(string="Comentarios del partido")

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
    
    @api.depends('fecha_hora')
    def _actualizar_estado(self):
        for record in self:
            if not record.fecha_hora:
                record.estado = "Pendiente"
            elif record.fecha_hora > fields.Datetime.now():
                record.estado = "Pendiente"
            else:
                tiempo_transcurrido = fields.Datetime.now() - record.fecha_hora
                if tiempo_transcurrido <= timedelta(minutes=105):
                    record.estado = "En curso"
                else:
                    record.estado = "Finalizado"
    
    @api.constrains('equipo_local', 'equipo_visitante')
    def _check_equipo_repetido(self):
        for record in self:
            if record.equipo_local == record.equipo_visitante:
                raise ValidationError("Un equipo no puede ser local y visitante al mismo tiempo.")

    @api.onchange('competicion')
    def _compute_equipos_competicion(self):
        if self.competicion:
            return {
                'domain': {
                    'equipo_local': [('id', 'in', self.competicion.listado_de_equipos.ids)],
                    'equipo_visitante': [('id', 'in', self.competicion.listado_de_equipos.ids)]
                }
            }
        else:
            return {
                'domain': {
                    'equipo_local': [],
                    'equipo_visitante': []
                }
            }
