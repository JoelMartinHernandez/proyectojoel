# -*- coding: utf-8 -*-
{
    'name': "proyectojoel",

    'summary': """
        Módulo de proyectoJoel""",

    'description': """
        aplicación personalizada que sirva de apoyo a una empresa de desarrollo de software
    """,

    'author': "Joel",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','project'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/res_config_settings_views.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'reports/proyectojoel_report.xml',
        'reports/proyectojoel_report_view.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'application': 'True',

    # assets
    'assets': {
        'web.assets_common': [
            'proyectojoel/static/src/scss/style1.scss',
        ],
        
    }
}
