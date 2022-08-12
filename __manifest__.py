# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Adev Profile',
    'version' : '1.0',
    'depends': ['base', 'sale', 'website_sale', 'sale_product_configurator'],
    'summary': 'Custom Developments',
    'description': """
    Custom addon made for developments
    """,
    'category': 'Few categories',
    'data': [
        'views/product_views.xml',
        'templates/configurator_template.xml'
    ],
    'demo': [
    ],
    'assets': {
        'web.assets_common': [
            'adev_profile/static/src/js/custom.js',
        ],
    },
    'installable': True,
    'application': True,
    # 'auto_install': False,
}
