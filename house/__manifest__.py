# -*- coding: utf-8 -*-
{
    'name': "house",

    'summary': """
        odoo doc training""",

    'description': """
       house module
    """,

    'author': "Glass Expansion",
    'website': "http://www.geicp.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/setting_view.xml',
        'views/offer.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}