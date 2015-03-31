#!/usr/bin/env python

"""
Commands related to syncing copytext from Google Docs.
"""

from fabric.api import task
from termcolor import colored
from re import search

import app_config
from etc.gdocs import GoogleDoc

@task(default=True)
def update():
    """
    Downloads a Google Doc as an Excel file.
    """
    if app_config.COPY_GOOGLE_DOC_URL == None:
        print colored('You have set COPY_GOOGLE_DOC_URL to None. If you want to use a Google Sheet, set COPY_GOOGLE_DOC_URL to the URL of your sheet in app_config.py', 'blue')
        return
    else:
        doc = {}
        url = app_config.COPY_GOOGLE_DOC_URL
        doc['key'] = search('(spreadsheets\/d\/|key=)(.*)(\/|&)', url).group(2)

        g = GoogleDoc(**doc)
        g.get_auth()
        g.get_document()

