# -*- coding: utf-8 -*-

from odoo import api
from odoo import exceptions
from odoo import fields
from odoo import models

class Activity(models.Model):
    _name = 'fctactivities.activity'

    name = fields.Char(string="Title", required=True)
    date = fields.Date(default=fields.Date.today)
    description = fields.Text()
    duration = fields.Float(digits=(6, 1), help="Duration in hours")
    remarks = fields.Text()
    owner = fields.Many2one('res.users', string="Pupil", default=lambda self: self.env.user, readonly=True)
    
    
    # 0 > duration <= 8
    @api.constrains('duration')
    def _check_activity_duration(self):
        for r in self:
            if r.duration > 8:
                raise exceptions.ValidationError("Activity duration can't surpass 8 hours.")
            elif r.duration <= 0:
                raise exceptions.ValidationError("Activity duration must be more than 0 hours.")
    
    # Activities duration total per day <= 8       
    @api.constrains('duration')
    def _check_day_duration(self):
        day_duration = 0
        for activity in self.search([('date', '=', self.date)]):
            day_duration = day_duration + activity.duration
            if day_duration > 8:
                raise exceptions.ValidationError('Activities duration total per day can\'t be more than 8 hours.')
                
    # Activities duration total per pupil <= 350              
    @api.constrains('duration')
    def _check_total_duration(self):
        total_duration = 0
        for activity in self.search([('owner', '=', self.owner.id)]):
            total_duration = total_duration + activity.duration
            if total_duration > 350:
                raise exceptions.ValidationError('Activities duration total per pupil can\'t be more than 350 hours.')