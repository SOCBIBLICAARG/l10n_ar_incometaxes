# -*- coding: utf-8 -*-
##############################################################################
#
#       Pere Ramon Erro Mas <pereerro@tecnoba.com> All Rights Reserved.
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Retenciones de ganancias de la República Argentina.',
    'version': '0.2.1',
    'author': 'Hernan Diego Broun (HDB) Elepe Argentina, Moldeo Interactive',
    'website': 'http://business.moldeo.coop',
    "category": "Accounting",
    "depends": ['account_voucher', 'l10n_ar_chart'],
    'update_xml': [
    'retenciones_view.xml',
    'retenciones_data.xml'
    ],
    'demo_xml': [],
    'active': False,
    'installable': True,
    'application': True,
}
