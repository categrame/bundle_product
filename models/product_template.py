# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_a_pack = fields.Boolean('Is a Pack', default=False)
    is_pack_confirmed = fields.Boolean()
    pack_line_ids = fields.Many2one(
        string="Product in the pack",
        comodel_name='product.product',
        help="Keep product for stock move"
    )