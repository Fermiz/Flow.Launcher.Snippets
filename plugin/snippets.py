# -*- coding: utf-8 -*-
"""
Snippets in Flowlauncher.

Simple plugin to save key/value snippets and copy to clipboard.
"""

from flowlauncher import FlowLauncher, FlowLauncherAPI
import sys
import ctypes
import sqlite3
import pyperclip

def getValue(dbName, key):
    value = {}
    conn = sqlite3.connect(dbName)
    cursor = conn.cursor()

    cursor.execute("SELECT value FROM snippets WHERE key=?", (key,))
    result = cursor.fetchone()
    if result:
        value = result[0]
    else:
        value = ""
    conn.close()
    return value

def saveValue(dbName, key, value):
    conn = sqlite3.connect(dbName)
    cursor = conn.cursor()
    cursor.execute("INSERT OR REPLACE INTO snippets (key, value) VALUES (?, ?)", (key, value))
    conn.commit()
    conn.close()
    copy2clip(dbName, value)

def deleteValue(dbName, key):
    conn = sqlite3.connect(dbName)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM  snippets WHERE key=?", (key,))
    conn.commit()
    conn.close()

def copy2clip(dbName, value):
    """Put snippets into clipboard."""
    pyperclip.copy(value)

class Snippets(FlowLauncher):

    def __init__(self, dbName):
        self.dbName = dbName
        super().__init__()
 
    def query(self, query):
        results = []
        try:
            if len(query.strip()) != 0:
                if ':' in query.strip():
                    key, value = query.strip().split(':', 1)
                    results.append({
                        "Title": "Save Code Snippet",
                        "SubTitle": "Key=" + key + ", Value=" + value,
                        "IcoPath": "assets/snippets.png", 
                        "ContextData": [key, value],
                        "JsonRPCAction": {"method": "save", "parameters": [key.strip(), value.strip()], }})
                else:
                    value = getValue(self.dbName, query.strip())
                    if len(value) != 0:
                        results.append({  
                            "Title": "⭐ " + query.strip(),
                            "SubTitle": "[Snippet] Copy to clipboard",
                            "IcoPath": "assets/snippets.png",
                            "ContextData": [query.strip(), value],
                            "JsonRPCAction": {"method": "copy", "parameters": [value], }})
                    else:
                        clipboardValue = pyperclip.paste()
                        displayValue = clipboardValue[:16] + "..." if len(clipboardValue) > 16 else ""
                        if len(clipboardValue) != 0:
                            results.append({
                                "Title": "Save from clipboard",
                                "SubTitle": "Key=" + query.strip() + ", Value=" + displayValue,
                                "IcoPath": "assets/snippets.png",
                                "ContextData": [query.strip(), clipboardValue],
                                "JsonRPCAction": {"method": "save", "parameters": [query.strip(), clipboardValue], }})

        except:
            value = sys.exc_info()
            print('Error opening %s: %s' % (value.filename, value.strerror))
            results.append({
                "Title": "Code Snippets Error",
                "SubTitle": "Please, Verify and try again",
                "IcoPath": "assets/snippets.png", "ContextData": "ctxData"})

        return results
    
    def context_menu(self, data):
        results = []
        results.append({
                        "Title": "Delete Code Snippet",
                        "SubTitle": "Key=" + data[0] + ", Value=" + data[1],
                        "IcoPath": "assets/snippets.png",
                        "JsonRPCAction": {"method": "delete", "parameters": [data[0]], }})
        results.append({
                "Title": "Save/Update Code Snippet",
                "SubTitle": "Key=" + data[0] + ", Value=" + data[1],
                "IcoPath": "assets/snippets.png", 
                "JsonRPCAction": {"method": "save", "parameters": [data[0], data[1]], }})
        return results

    def copy(self, value):
        """Copy Snippets to clipboard."""
        copy2clip(self.dbName, value)

    def save(self, key, value):
        """Save Snippets into sqlite"""
        saveValue(self.dbName, key.strip(), value.strip())

    def delete(self, key):
        """Delete Snippets from sqlite"""
        deleteValue(self.dbName, key.strip())

if __name__ == "__main__":
    Snippets()
