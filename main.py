# -*- coding: utf-8 -*-
"""
Snippets in Flowlauncher.

Simple plugin to save key/value snippets and copy to clipboard.
"""

import os
import sys
import sqlite3

# add plugin to local PATH
parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))

from plugin.snippets import Snippets

db_name = "./snippets.db"

if __name__ == "__main__":
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS snippets (key TEXT PRIMARY KEY, value TEXT)''')
    conn.commit()
    conn.close()
    Snippets()
