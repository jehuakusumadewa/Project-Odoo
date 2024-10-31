{
    'name': 'Module Custom Pemesanan',
    'version': '18.0',
    'category': 'purchase',
    'summary': 'Pemesanan Custom Module',
    'description': """
        Pemesanan Custom Module by Jehua
    """,
    'website': '',
    'author': 'Jehua Dewa',
    'depends': ['web', 'base'],
    'data': [
        'data/sequence_data.xml',
        'views/master_ruangan_view.xml',
        'views/pemesanan_view.xml',
        'views/pemesanan_action.xml',
        'views/pemesanan_menuitem.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'license': 'OEEL-1',
}
