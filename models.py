from odoo import tools, models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import date,datetime


class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    @api.model
    def default_get(self, fields):
        res = super(SaleAdvancePaymentInv, self).default_get(fields)
        order_id = self.env.context.get('active_id')
        order = self.env['sale.order'].browse(order_id)
        for order_line in order.order_line:
            if order_line.qty_delivered == 0:
                if order_line.product_id.qty_available < 1:
                    raise ValidationError('No se puede facturar porque no hay stock para %s'%(order_line.product_id.name))
        return res
