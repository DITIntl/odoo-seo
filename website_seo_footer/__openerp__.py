# -*- coding: utf-8 -*-
# Copyright 2018 Xavier Brochard
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
{
    'name': 'SEO Footer',
    'summary': 'Remove heading tags and obfuscate default links in footer (Page Rank Sculpture).',
    'version': '9.0.1.0.0',
    'category': 'Website',
    'website': 'https://zeroheure.info/',
    'support' : 'support@zeroheure.info',
    'author': 'Xavier Brochard, zeroheure.info',
    'license': 'LGPL-3',
    'images': ['static/description/module_image.png'],
    'application': False,
    'installable': True,
    'depends': [
        'website',
    ],
    'data': [
        'views/seo_footer.xml',
        'views/assets.xml',
    ],
}
