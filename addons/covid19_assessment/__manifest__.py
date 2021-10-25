# -*- coding: utf-8 -*-
{
    'name': "covid19_assessment",

    'summary': """
    Website form for Covid19
    """,

    'description': """
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Website/Website',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/covid_email_template.xml',
        'views/covid_website_menu.xml',
        'views/covid_website_form.xml',
        'views/thank_you_page.xml',
    ],
}
