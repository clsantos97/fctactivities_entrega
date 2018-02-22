# -*- coding: utf-8 -*-
{
    'name': "FCT Activities",

    'summary': """Manage FCT Activities""",

    'description': """
        Module for managing FCT Activities:
            - Activities.
            - Pupils.
            - Tutor.
            - FCT Partner.
    """,

    'author': "Carlos Santos",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'report'],

    # always loaded
    'data': [
        'security/user_groups.xml',
        'security/ir.model.access.csv',
        'views/user.xml',
        'views/fctactivities.xml',
        'views/templates.xml',
        'views/partner.xml',
        'views/activity_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}