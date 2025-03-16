{
    "name": "Branding APIS",
    "version": "1.0",
    "summary": "Custom branding for APIS",
    "description": "Adds custom branding to the APIS user interface.",
    "category": "Themes/Backend",
    'website': 'https://ultrasoft.mk',
    'author': 'Ultrasoft Systems',
    'depends': ['base', 'web'],
    'data': [
        'views/custom_res_config_settings_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            "custom_branding/static/src/xml/custom_navbar.xml",
            "custom_branding/static/src/xml/custom_settings_branding.xml",
            "custom_branding/static/src/css/custom.css",
        ],
        'web.assets_frontend': [
        ]
    },
    "installable": True,
    'application': False,
    'auto_install': True,
    'license': 'LGPL-3',
}
