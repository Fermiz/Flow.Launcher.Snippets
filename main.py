# -*- coding: utf-8 -*-
"""
Snippets in Flowlauncher.

Simple plugin to save key/value snippets and copy to clipboard.
"""

import os
import sys
import sqlite3

# add plugin to local PATH
parentFolderPath = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parentFolderPath)
sys.path.append(os.path.join(parentFolderPath, 'lib'))
sys.path.append(os.path.join(parentFolderPath, 'plugin'))

from plugin.snippets import Snippets

if __name__ == "__main__":
    pluginPath = os.path.abspath(os.path.dirname(parentFolderPath))
    mainPath = os.path.abspath(os.path.dirname(pluginPath))
    snippetSettingsPath = mainPath + "/Settings/Plugins/Flow.Launcher.Snippets"
    
    dbName = snippetSettingsPath + "/snippets.db"

    if not (os.path.exists(snippetSettingsPath)):
        os.makedirs(snippetSettingsPath)
        dbName = snippetSettingsPath + "/snippets.db"
        conn = sqlite3.connect(dbName)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS snippets (key TEXT PRIMARY KEY, value TEXT)''')
        conn.commit()
        conn.close()
    
    Snippets(dbName=dbName)
