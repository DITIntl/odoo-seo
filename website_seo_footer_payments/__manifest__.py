# -*- coding: utf-8 -*-
# Copyright 2018 Xavier Brochard
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
{
    "name": "SEO Footer Payments",
    "summary": "Remove Heading tag and obfuscate additional links in footer.",
    "version": "10.0.1.0.0",
    "category": "Website",
    "website": "https://zeroheure.info/",
    "support" : "support@zeroheure.info",
    "author": "Xavier Brochard, zeroheure.info",
    "license": "LGPL-3",
    "price":"100",
    "currency":"EUR",
    "images": ['images/main_screenshot.png'],
    "application": False,
    "installable": True,
    "depends": [
        "website_payment",
        "website_seo_footer",
    ],
    "data": [
        "views/templates.xml",
    ],
}
