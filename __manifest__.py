# -*- coding: utf-8 -*-
{
    'name': "Real Estate CI",

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
    'version': '16.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/real_estate_ci.xml',
        'security/ir.model.access.csv',
        'views/locataire_views.xml',
        'views/location_views.xml',
        'views/proprietaire_views.xml',
        'views/propriete_views.xml',
        'views/type_de_propriete_views.xml',
        'views/real_estate_ci_views.xml',
    ],

}
