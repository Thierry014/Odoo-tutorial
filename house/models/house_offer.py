
from odoo import api, fields, models
from odoo.exceptions import ValidationError, UserError


class HouseOffer(models.Model):
    _name = 'house.offer'
    _description = 'some offers'


    buyer_id = fields.Many2one(comodel_name='res.partner', string='')
    offer_price = fields.Float(string='Offer Price', digits=(10,0))
    state = fields.Selection(string='Status', selection=[('draft','Draft'),('rejected', 'Rejected'), ('accepted', 'Accepted')])
    
    house_id = fields.Many2one(comodel_name='house.house', string='')
    
    
    def accept_offer(self):
        for r in self:
            all_offers = self.search([('house_id','=',r.house_id.id)])
            print(all_offers)
            for offer in all_offers:
                offer.state = 'rejected'
            
            r.state = 'accepted' 
            r.house_id.state = 'confirmed'
            r.house_id.buyer = r.buyer_id
            r.house_id.selling_price = r.offer_price
    
    
    def reject_offer(self):
        for r in self:
            r.state = 'rejected'
            
    
    # inherit function 
    @api.model
    def create(self,vals):
        property_id = self.env['house.house'].browse(vals['house_id'])
        if len(property_id.offer_ids):
            if vals['offer_price'] < min(property_id.offer_ids.mapped('offer_price')):
                raise UserError("We don't accepet offer lower than current price")
        
        return super().create(vals)