# -*- coding: utf-8 -*-

from odoo import fields, models


# class ResConfigSettings(models.TransientModel):
#     _inherit = 'res.config.settings'

#     checkbox = fields.Boolean(string='Pronto acabara todo', config_parameter="proyectojoel.checkbox")


# class ResConfigSettings(models.TransientModel):
#     _inherit = 'res.config.settings'

#     delay_alert_contract = fields.Boolean(string='Pronto acabara todo ahora es personal')
#     dropdown_field = fields.Selection([
#         ('option1', 'Contenido 1'),
#         ('option2', 'Elemento 2'),
#         ('option3', 'Opcion 3'),
#     ], string='Dropdown Field')

# class ResConfigSettings(models.TransientModel):
#    _inherit = 'res.config.settings'
#    contract_type = fields.Selection(
#        [('monthly', 'Monthly'), ('half_yearly', '6 Months'),
#         ('yearly', 'Yearly')],
#        string="Contract Type",
#        config_parameter='employee_contract.contract_type',
#        help="Select contract types from the selection field")