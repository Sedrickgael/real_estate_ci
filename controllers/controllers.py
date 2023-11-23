# -*- coding: utf-8 -*-
# from odoo import http


# class RealEstateCi(http.Controller):
#     @http.route('/real_estate_ci/real_estate_ci', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/real_estate_ci/real_estate_ci/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('real_estate_ci.listing', {
#             'root': '/real_estate_ci/real_estate_ci',
#             'objects': http.request.env['real_estate_ci.real_estate_ci'].search([]),
#         })

#     @http.route('/real_estate_ci/real_estate_ci/objects/<model("real_estate_ci.real_estate_ci"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('real_estate_ci.object', {
#             'object': obj
#         })
