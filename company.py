# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
import datetime
from datetime import date
#import account 
from openerp import netsvc
from openerp.osv import fields, osv
from openerp.tools.translate import _
import logging



class res_company(osv.osv):
    _name = "res.company"
    _inherit = "res.company"
    _description = "Inherit company"
    _columns = {
        'tax_withholding_ids': fields.one2many('account.tax.withhold', 'res_company_id', string='Impuesto a retener')
    }
    # _sql_constraints = [('res_company_constraint', 'unique(tax_withholding_ids)', 'Impuesto a retener must be unique!')]

res_company()
