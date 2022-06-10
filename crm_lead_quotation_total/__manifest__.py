# -*- coding: utf-8 -*-
{
    'name': 'crm_lead_quotation_total',
    'version': '13.0.1.0.0',
    'summary': 'Agrega un campo para el total neto (Base imponible) de presupuestos realizados.',
    'description': 'Agrega un campo para el total neto (Base imponible) de presupuestos realizados.',
    'category': 'Crm',
    'author': 'Balmes92',
    'company': 'Balmes92',
    'contributors':  ['Juan Pablo Garza <jp@balmes92.com>'],
    'website': 'https://www.balmes92.com',
    'license': 'AGPL-3',
    'depends': [
                'sale_management',
                'sale_crm',
        ],
    'data': [
        'views/crm_lead_views.xml',
        ],        
    'installable': True,
    'auto_install': False,
}
