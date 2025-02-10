import sys
import os

from odoo import models, api, exceptions

class Restart(models.TransientModel):
    _name = 'practica.restart'
    _description = 'Restart'

    @api.model
    def do_restart(self):
        if self.env.user.has_group('base.group_system'):
            try:
                self.env.cr.commit()
                self.env.cr.close()
                os.execv(sys.executable, ['python3'] + sys.argv)
            except Exception as e:
                raise exceptions.UserError(f"Error al reiniciar Odoo: {e}")
        else:
            raise exceptions.AccessError("No tienes permiso para reiniciar Odoo")