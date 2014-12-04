# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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
# Coded by: Said Kuri Nunez (skuri@tantums.com)
##############################################################################

import datetime
from openerp.osv import fields, osv,orm
import pdb
from openerp.tools.translate import _
	

class report_simple_account_statement_wizard(orm.TransientModel):
	_name = 'report.simple.account.statement.wizard'
	_columns = {
	'centro_costo_id': fields.many2one('account.move.line', string="Cost Center"),
	'account_id': fields.many2one('account.account',string="Account"),
	'partner_id': fields.many2one('res.partner',domain=[('supplier','=',True)], string="Supplier"),
	'period_id': fields.many2one('account.period', string="Period",required=True),
	}

	def print_report(self,cr,uid,ids,context=None):
		datas = {}
		datas = {'ids': context.get('active_ids', [])}
		datas['model'] = 'simple.account.statement.wizard'
		datas['form'] = self.read(cr, uid, ids)[0]
		return {
			'type': 'ir.actions.report.xml',
			'report_name': 'simple.account.statement',
			'datas':datas,		
			'report_type' : 'webkit',
		}