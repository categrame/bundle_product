# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import http
from odoo.http import request

from odoo.addons.website_sale.controllers.variant import WebsiteSaleVariantController


class WebsiteSaleVariantControllerCustom(WebsiteSaleVariantController):
    @http.route(['/sale/get_combination_info_website'], type='json', auth="public", methods=['POST'], website=True)
    def get_combination_info_website(self, product_template_id, product_id, combination, add_qty, **kw):
        res = super(WebsiteSaleVariantControllerCustom, self).get_combination_info_website(product_template_id, product_id, combination, add_qty, **kw)
        product_template = request.env['product.template'].browse(product_template_id)
        print(kw)
        if kw.get('original_template_id') and kw.get('product_from_pack'):
            product = request.env['product.product'].browse(product_id)
            print(product.display_name)
        # product_from_pack
        # original_template_id
        # import pdb
        # pdb.set_trace()
        return res
