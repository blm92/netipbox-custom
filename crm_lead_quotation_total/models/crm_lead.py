# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from dateutil.relativedelta import relativedelta

from odoo import api, fields, models


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    quotation_amount_total = fields.Monetary(compute='_compute_quotation_amount_total', 
                                            string="Total de presupuestos", 
                                            help="Total neto (Base imponible) de presupuestos realizados", 
                                            currency_field='company_currency')

    @api.depends('order_ids.state', 'order_ids.currency_id', 'order_ids.amount_untaxed', 'order_ids.date_order', 'order_ids.company_id')
    def _compute_quotation_amount_total(self):
        for lead in self:
            total = 0.0
            company_currency = lead.company_currency or self.env.company.currency_id
            for order in lead.order_ids:
                if order.state in ('draft', 'sent'):
                    total += order.currency_id._convert(
                        order.amount_untaxed, company_currency, order.company_id, order.date_order or fields.Date.today())
            lead.quotation_amount_total = total
        