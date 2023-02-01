# -*- coding: utf-8 -*-


from odoo import fields, models,tools,api, _

class PosOrderLine(models.Model):
    _inherit = 'pos.order.line'

    def _order_line_fields(self, line, session_id=None):
        res = super(PosOrderLine, self)._order_line_fields(line, session_id)
        prod = line[2]
        product = self.env['product.product'].search([('id', '=', prod['product_id'])])
        if product.allow_bom_pro:
            if prod['qty'] > 0:
                bom_count = self.env['mrp.bom'].search([('product_tmpl_id', '=', product.product_tmpl_id.id)])
                if bom_count:
                    bom_temp = self.env['mrp.bom'].search([('product_tmpl_id', '=', product.product_tmpl_id.id),
                                                           ('product_id', '=', False)])
                    bom_prod = self.env['mrp.bom'].search([('product_id', '=', prod['product_id'])])
                    if bom_prod:
                        bom = bom_prod[0]
                    elif bom_temp:
                        bom = bom_temp[0]
                    else:
                        bom = []
                    if bom:
                        vals = {
                            'origin': prod['name'],
                            'state': 'confirmed',
                            'product_id': product.id,
                            'product_tmpl_id': product.product_tmpl_id.id,
                            'product_uom_id': product.uom_id.id,
                            'product_qty': prod['qty'],
                            'bom_id': bom.id,
                        }
                        mp = self.env['mrp.production'].sudo().create(vals)
                        mp._onchange_move_raw()
        return res

class ProductTemplate(models.Model):
    _inherit = "product.template"

    allow_bom_pro = fields.Boolean("Allow BOM Product In POS")


