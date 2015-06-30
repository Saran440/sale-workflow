# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015 AKRETION (<http://www.akretion.com>).
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

{
    'name': 'Sales Team Invoice Partner',
    'version': '1.0',
    'category': 'Sales Management',
    'summary': 'Adds invoice partner in sales team for use in a sale order',
    'author': 'Akretion, Odoo Community Association (OCA)',
    'website': 'http://www.akretion.com/',
    'license': 'AGPL-3',
    'depends': [
        'sales_team',
        'sale'
    ],
    'data': [
        'sales_team_view.xml',
        'sale_view.xml',
    ],
    'demo': [
        'demo/sale.xml',
    ],
    'installable': True,
}
