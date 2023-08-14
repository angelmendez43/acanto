from odoo import models, fields

class AcantoVoucher(models.Model):
    _name = 'acanto.voucher'
    _description = 'Voucher'

    recibimos_id = fields.Many2one('res.partner',string="Recibimos de")
    factura = fields.Char(string='Factura')
    descripcion = fields.Char(string='Descripcion')
    fecha = fields.Date(string='Fecha')
    voucher_no = fields.Char(string='Voucher No')
    cantidad_pago = fields.Float(string='Cantidad')
    banco_id = fields.Many2one('account.journal',string="Banco")
    cuenta_cheque = fields.Float(string='Cuenta No.')
    orden = fields.Char(string='A la orden de')
    cheque_no = fields.Char(string='No.')
    cantidad_cheque = fields.Float(string='Cantidad')
    elaborado = fields.Char(string='Elaborado por')
    autorizado = fields.Char(string='Autorizado por')
    recibido = fields.Char(string='Recibido por')
