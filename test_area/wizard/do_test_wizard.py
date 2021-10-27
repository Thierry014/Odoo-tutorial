from datetime import date
from odoo import api, fields, models


class TestWizard(models.TransientModel):
    _name = 'test.test.wizard'
    _description = 'do test here'

    # result = fields.Boolean(string='X')
    
    test_id = fields.Many2one(comodel_name='test.test', string='Test')
    test_desc = fields.Text(string='Test Note')
    test_date = fields.Date(string='Test Date', default=date.today())
    
    
    
    def do_test_wizard(self):
        for r in self:
            test = r.test_id
            test.state = 'tested'
            # update test informatino as well
            test.test_info = r.test_desc
            test.test_date = r.test_date
            print('test done')