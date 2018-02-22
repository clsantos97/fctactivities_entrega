# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Partner(models.Model):
    _inherit = 'res.partner'
    isFCTPartner = fields.Boolean("FCTPartner", default=False)
    
    pupil_ids = fields.One2many('res.users','fctpartner', string="Pupils")