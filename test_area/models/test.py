# -*- coding: utf-8 -*-


from odoo import api, fields, models


class TestTest(models.Model):
    _name = 'test.test'
    _description = 'test something in this module'

    name = fields.Char(string='Name')
    test_no = fields.Char(string='TestNo')
    
    test_people_id = fields.Many2one(comodel_name='test.people', string='People')
    test_staff_id = fields.Many2one(comodel_name='test.staff', string='Staff')
    test_area_id = fields.Many2one(comodel_name='test.area', string='Area')
    test_result = fields.Boolean(string='Covid Postive', default=False)
    
    test_info = fields.Text(string='Test INfo')
    test_date = fields.Date()
    
    state = fields.Selection(string='', selection=[('reg', 'Reg'), ('tested', 'Tested'),('done', 'Done'),('cancelled','Cancelled')], default = 'reg')
    
    
    def do_test(self):
        # popup wizard form to launch the testing 
        print(self._context)
        res = {
            'name': 'Dping Test',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'test.test.wizard',
            'view_id': self.env.ref('test_area.do_test_wizard_form_view').id,
            'type': 'ir.actions.act_window',
            'context':{
                # 'default_test_id':self._context['params']['id'],
                'default_test_id':self.id
            },
            'target': 'new'
        }
        return res
    
    def input_result(self):
        res ={
            'name': 'Test res',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'test.resinput.wizard',
            'view_id': self.env.ref('test_area.input_res_wizard_form_view').id,
            'type': 'ir.actions.act_window',
            'context':{
                'default_test_id':self.id
            },
            'target': 'new'
        }
        return res

    
    def print_test_report(self):
        for r in self:
            print(f'{r.name} is printed')
            return self.env.ref('test_area.report_covid_test_report').report_action(self)

 

    
    

##########################################################################################################################

class TestPeople(models.Model):
    _name = 'test.people'
    _description = 'New Description'

    name = fields.Char(string='Name')
    age = fields.Integer(string='Age')
    current_state = fields.Boolean(string='Pos?', default=False)
    
    
    test_record_ids = fields.One2many(comodel_name='test.test', inverse_name='test_people_id', string='Test Record')
    
    
    
##########################################################################################################################


class TestArea(models.Model):
    _name = 'test.area'
    _description = 'New Description'

    name = fields.Char(string='Name')

    
    
##########################################################################################################################

class TestStaff(models.Model):
    _name = 'test.staff'
    _description = 'New Description'

    name = fields.Char(string='Name')
##########################################################################################################################


    