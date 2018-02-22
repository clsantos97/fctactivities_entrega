# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models

class Users(models.Model):
    _inherit = 'res.users'
    isPupil = fields.Boolean("Pupil", default=False)
    isTutor = fields.Boolean("Tutor", default=False)
    
    activities = fields.One2many('fctactivities.activity', 'owner', string="Activities")
    tutor = fields.Many2one('res.users', string="Tutor")
    pupils = fields.One2many('res.users', 'tutor', string="Pupils")
    fctpartner = fields.Many2one('res.partner', string="FCTPartner")

    @api.constrains('isPupil', 'isTutor')
    def _check_pupil_not_tutor(self):
        for r in self:
            if r.isPupil == True & r.isTutor == True:
                raise exceptions.ValidationError("A user must be either a Pupil or a Tutor.")
    
            


