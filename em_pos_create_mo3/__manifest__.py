# -*- coding: utf-8 -*-

{
    'name': 'POS create Manufacturing Order.',
    'version': '1.0',
    'category': 'Point of Sale',
    'sequence': 6,
    'author': 'ErpMstar Solutions',
    'summary': "Allows to create manufacturing order when you select BOM product." ,
    'description': "Allows to create manufacturing order when you select BOM product.",
    'depends': ['point_of_sale','mrp'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        # 'views/templates.xml',
        # 'views/sequence.xml',
    ],
    'qweb': [
        # 'static/src/xml/pos.xml',
    ],
    'images': [
        'static/description/mo.jpg',
    ],
    'installable': True,
    'website': '',
    'auto_install': False,
    'price': 29,
    'currency': 'EUR',
}
