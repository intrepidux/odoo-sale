# -*- coding: utf-8 -*-

from odoo import api, fields, models, modules, _
from odoo.exceptions import ValidationError

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    license_duration = fields.Integer(string="Duration", help="The duration in days")
    form_of_agreement = fields.Char(
        string="Form of agreement", help="Form of agreement")
