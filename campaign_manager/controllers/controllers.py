# -*- coding: utf-8 -*-
# from odoo import http


# class CampaignManager(http.Controller):
#     @http.route('/campaign_manager/campaign_manager', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/campaign_manager/campaign_manager/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('campaign_manager.listing', {
#             'root': '/campaign_manager/campaign_manager',
#             'objects': http.request.env['campaign_manager.campaign_manager'].search([]),
#         })

#     @http.route('/campaign_manager/campaign_manager/objects/<model("campaign_manager.campaign_manager"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('campaign_manager.object', {
#             'object': obj
#         })
