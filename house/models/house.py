# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta


class House(models.Model):
    _name = 'house.house'

    # top group
    name = fields.Char('Title')
    postcode = fields.Integer('Postcode', group_operator=False)
    exepted_price = fields.Float(string='Excepeted Price', digits=(10,0))
    ava_from = fields.Date(string='Available From', default=date.today()+relativedelta(months=+3))
    selling_price = fields.Float(string='Selling Price', readobly=True, group_operator=False)
    property_type = fields.Many2one(comodel_name='house.type', string='Property type')
    tag_ids = fields.Many2many(comodel_name='house.tag', string='')
    best_price = fields.Float(string='Best Offer', compute='_get_best_offer', inverse='_inverse_best_offer', digits=(10,0))
    
    
    
    # page 1
    description = fields.Text('Description')
    bedroom = fields.Integer(string='Bedroom(s)', group_operator=False, default=3 )
    bathroom = fields.Integer(string='Bathroom(s)', default=2)
    garden = fields.Boolean(string='Garden')
    garage = fields.Boolean(string='Garage')
    active = fields.Boolean(string='Active', default=True)
    
    
    # header
    state = fields.Selection(string='', selection=[('cancelled', 'Cancelled'), 
                                                   ('draft', 'Draft'), 
                                                   ('offered', 'Offered'), 
                                                   ('confirmed', 'Confirmed'), 
                                                   ('sold', 'Sold')], default='draft')
    
    # page 2
    salesman = fields.Many2one(comodel_name='res.users', string='Salesman', default = lambda self: self.env.user)
    buyer = fields.Many2one(comodel_name='res.partner', string='buyer')
    
    # page3
    offer_ids = fields.One2many(comodel_name='house.offer', inverse_name='house_id', string='')
    offer_count = fields.Integer(string='', compute='_get_offer_count')
    
    
    # computed function
    @api.depends("offer_ids")
    def _get_offer_count(self):
        for r in self:
            r.offer_count = len(r.offer_ids)
        
    
    
    # odoo function
    @api.depends("offer_ids")
    def _get_best_offer(self):
        for r in self:
            price_list = r.offer_ids.mapped('offer_price')
            if price_list:
                r.best_price = max(price_list)
        
    def _inverse_best_offer(self):
        print('>>>inverse<<<')
        # use with store = True computed field 
    
    def mark_as_sold(self):
        print('call in House')

    def mark_as_cancelled(self):
        ...
    
    
    @api.constrains('selling_price')
    def _check_selling_price(self):
        for r in self:
            if r.selling_price < r.exepted_price * 0.9:
                raise ValidationError('No deal')

    
    # inherit function 
    def unlink(self):
        if self.state not in ['cancelled']:
            raise UserError('Adv can only be removed when its cancelled')
        
        return super().unlink()


    def action_house_offer(self):
        return{

        }