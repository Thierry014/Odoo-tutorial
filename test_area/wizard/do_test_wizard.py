from odoo import api, fields, models


class TestWizard(models.TransientModel):
    _name = 'test.test.wizard'
    _description = 'do test here'

    result = fields.Boolean(string='X')
    
    test_id = fields.Many2one(comodel_name='test.test', string='Test')
    
    def do_test_wizard(self):
        print('test done')