# -*- coding: utf-8 -*-
"""
Snippets in Flowlauncher.

Simple plugin to save key/value snippets and copy to clipboard.
"""

from flowlauncher import FlowLauncher, FlowLauncherAPI
import sys
import subprocess
import sqlite3

db_name = "./snippets.db"

def getValue(key):
    value = {}
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("SELECT value FROM snippets WHERE key=?", (key,))
    result = cursor.fetchone()
    if result:
        value = result[0]
    else:
        value = ""
    conn.close()
    return value

def saveValue(key, value):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("INSERT OR REPLACE INTO snippets (key, value) VALUES (?, ?)", (key, value))
    conn.commit()
    conn.close()
    cmd = 'echo '+ value +'|clip'
    return subprocess.check_call(cmd, shell=True)

def copy2clip(txt):
    """Put snippets into clipboard."""
    cmd = 'echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)


class Snippets(FlowLauncher):

    def query(self, query):
        results = []
        try:
            if len(query.strip()) != 0:
                if ':' in query.strip():
                    key, value = query.strip().split(':', 1)
                    results.append({
                        "Title": "Save Snippets",
                        "SubTitle": "key=" + key + ", Value=" + value,
                        "IcoPath": "assets/snippets.png", 
                        "ContextData": "ctxData",
                        "JsonRPCAction": {"method": "save", "parameters": [key.strip(), value.strip()], }})
                else:
                    value = getValue(query.strip())
                    if len(value) != 0:
                        results.append({ 
                            "Title": "Saved⭐ " + query.strip(),
                            "SubTitle": "Copy snippets value into clipboard",
                            "IcoPath": "assets/snippets.png",
                            "ContextData": "ctxData",
                            "JsonRPCAction": {"method": "copy", "parameters": [value], }})

        except:
            # value = sys.exc_info()
            # print('Error opening %s: %s' % (value.filename, value.strerror))
            results.append({
                "Title": "Code Snippets Error",
                "SubTitle": "Please, Verify and try again",
                "IcoPath": "assets/snippets.png", "ContextData": "ctxData"})

        return results

    def copy(self, ans):
        """Copy Snippets to clipboard."""
        FlowLauncherAPI.show_msg("Copied to clipboard", copy2clip(ans))

    def save(self, key, value):
        """Save Snippets into sqlite"""
        FlowLauncherAPI.show_msg("Saved snippets", saveValue(key.strip(), value.strip()))


if __name__ == "__main__":
    Snippets()
