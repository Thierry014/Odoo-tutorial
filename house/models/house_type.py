
from odoo import api, fields, models


class HouseType(models.Model):
    _name = 'house.type'
    _description = 'house, apartment, penthouse, castle'

    name = fields.Char(string='Name')
    house_ids = fields.One2many(comodel_name='house.house', inverse_name='property_type', string='Property', compute='_get_house_from_type')
    
    offer_count = fields.Integer(string='' , compute='_get_offer_num')
    
    
    def _get_house_from_type(self):
        for r in self:
            r.house_ids = self.env['house.house'].search([('property_type','=',r.id)])
    
    
    def _get_offer_num(self):
        for r in self:
            r.offer_count = self.env['house.offer'].search_count([('house_id.property_type','=',r.id)])


    def action_type_offer(self):
        return {
            'name': 'Offers',# name can be anything
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'house.offer',
            'type': 'ir.actions.act_window',
            'domain': [('house_id.property_type','in', [self.id])],
        }




class HouseTag(models.Model):
    _name = 'house.tag'
    _description = 'cozy, double, single, location etc...'

    name = fields.Char(string='Name')
    color = fields.Integer(string='Color No')
    
