# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Stage(models.Model):
    _inherit = "crm.stage"

    esta_perdida = fields.Boolean('¿Está en la etapa perdida?')
