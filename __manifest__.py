# -*- coding: utf-8 -*-
{
    'name': "trabajo_final",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'data/sequences.xml',
        #'security/ir.model.access.csv',
        'views/division.xml',
        'views/trainer.xml',
        'views/team_sport_division.xml',
        'views/status.xml',
        'views/position.xml',        
        'views/player.xml',
        'views/team.xml',
        'views/competicion.xml',
        'views/arbitro.xml',
        'views/partido.xml',
        'views/deporte.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'DAM/static/css/style.scss',
        ],
        'web.assets_frontend': [
            'DAM/static/css/style.scss',
        ],
    },
}
