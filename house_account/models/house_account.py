from datetime import date
from odoo import api, fields, models
from odoo.exceptions import ValidationError, UserError


class House(models.Model):
    _inherit = 'house.house'

    # inherit function from parernt model 
    def mark_as_sold(self):
        for r in self:
            if r.state not in ['confirmed']:
                raise UserError(f"Can't not sold, in {r.state} state")
            
        print(f"call in link function")
        self.state = 'sold'
        # create a invoice 
        self.create_invoice()
        
        
        return super().mark_as_sold()

    
    # odoo function 
    
    @api.multi
    def create_invoice(self):
        # get account_invoice object 
        inv_obj = self.env['account.invoice']
        
        invoice_lines = [] #should be [(0,0,{line1}),{line2}]
        
        # self._get_invoice_line_from_house()
        line = (0,0,{
            'quantity': 1,
            'name': self.name,
            'price_unit': self.selling_price,
            'account_id':self.env['account.account'].browse('1').id,
        })
        
        service_fee_line = (0,0,{
            'quantity': 1,
            'name': 'Service fee',
            'price_unit': 100,
            'account_id':self.env['account.account'].browse('1').id,
        })
        
        invoice_lines.extend([line,service_fee_line])
        
        
        # prepare the invoice
        invoice_rec = {
            'partner_id':self.buyer.id,
            'parent_id':self.salesman.id,
            'currency_id':21,
            'name':f'{self.name} invoice',
            'type': 'out_invoice',
            'account_id':self.env['account.account'].browse('1').id,
            'invoice_line_ids': invoice_lines,
            'date_invoice':date.today(),

        }
        # acc_inv.create(invoice_vals)
        
        inv_obj.create(invoice_rec)
        print('<<< Invoice create >>>')