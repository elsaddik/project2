# -*- coding: utf-8 -*-
# from odoo import http


# class Project2(http.Controller):
#     @http.route('/project2/project2', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project2/project2/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('project2.listing', {
#             'root': '/project2/project2',
#             'objects': http.request.env['project2.project2'].search([]),
#         })

#     @http.route('/project2/project2/objects/<model("project2.project2"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project2.object', {
#             'object': obj
#         })
