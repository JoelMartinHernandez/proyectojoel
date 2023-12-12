# -*- coding: utf-8 -*-
# from odoo import http


# class Proyectojoel(http.Controller):
#     @http.route('/proyectojoel/proyectojoel', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/proyectojoel/proyectojoel/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('proyectojoel.listing', {
#             'root': '/proyectojoel/proyectojoel',
#             'objects': http.request.env['proyectojoel.proyectojoel'].search([]),
#         })

#     @http.route('/proyectojoel/proyectojoel/objects/<model("proyectojoel.proyectojoel"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('proyectojoel.object', {
#             'object': obj
#         })
