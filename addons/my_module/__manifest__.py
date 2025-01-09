#defines file as a odoo module 
{
    'name': "my_module",
    'version': '1.0',
    'depends': ['base'],
    'author': "Kim Vuorenpää",
    'category': 'Category',
    'description': """
    Technical support specialist Assigment - 09.01.2025
    """,
    # data files always loaded at installation
    'data': [
        'views/mymodule_view.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        'demo/demo_data.xml',
    ],
}