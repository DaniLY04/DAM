# -*- coding: utf-8 -*-
# from odoo import http


# class TrabajoFinal(http.Controller):
#     @http.route('/trabajo_final/trabajo_final', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/trabajo_final/trabajo_final/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('trabajo_final.listing', {
#             'root': '/trabajo_final/trabajo_final',
#             'objects': http.request.env['trabajo_final.trabajo_final'].search([]),
#         })

#     @http.route('/trabajo_final/trabajo_final/objects/<model("trabajo_final.trabajo_final"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('trabajo_final.object', {
#             'object': obj
#         })
