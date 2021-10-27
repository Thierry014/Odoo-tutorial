from datetime import date
from odoo import api, fields, models

class ResInputWizard(models.TransientModel):
    _name = 'test.resinput.wizard'
    _description = 'result here'
    
    test_id = fields.Many2one(comodel_name='test.test', string='Test')
    test_people = fields.Many2one(comodel_name='test.people', string='People', related='test_id.test_people_id')
    
    def test_pos(self):
        for r in self:
            r.test_id.state = 'done'
            r.test_id.test_result = True
            r.test_id.test_people_id.current_state=True
    
    def test_neg(self):
        for r in self:
            r.test_id.state = 'done'
            r.test_id.test_people_id.current_state=False
