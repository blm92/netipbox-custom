# Copyright 2015 Tecnativa - Pedro M. Baeza
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import fields, models


class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    amount_in = fields.Monetary('Ingreso', compute="_compute_in_out",store=True)
    amount_out = fields.Monetary('Egreso', compute="_compute_in_out",store=True)
    margen = fields.Monetary('Margen', compute="_compute_in_out",store=True)


    def _compute_in_out(self):
        for rec in self:
            rec.amount_in = 0
            rec.amount_out = 0
            if rec.amount >= 0:
                rec.amount_in = rec.amount
            else:
                rec.amount_out = - rec.amount
            rec.margen = rec.amount