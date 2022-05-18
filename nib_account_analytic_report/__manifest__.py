# -*- coding: utf-8 -*-
{
    'name': 'nib_account_analytic_report',
    'version': '13.0.1.0.0',
    'summary': 'Modificaciones para mejorar el reporting de la contabilidad analítica.',
    'description': 'Modificaciones para mejorar el reporting de la contabilidad analítica.',
    'category': 'Contabilidad',
    'author': 'Balmes92',
    'company': 'Balmes92',
    'contributors':  ['Juan Pablo Garza <jp@balmes92.com>'],
    'website': 'https://www.balmes92.com',
    'license': 'AGPL-3',
    'depends': [
            'analytic',
        ],
    'data': [
        'views/account_analytic_views.xml',
        ],        
    'installable': True,
    'auto_install': False,
}
