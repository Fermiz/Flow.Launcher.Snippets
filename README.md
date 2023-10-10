# Flow.Launcher.Snippets

This Snippets plugin let you save key/value snippets and copy to clipboard copy it from [Flow Launcher](https://www.flowlauncher.com/).

## How to use it

1. Install this plugin via `pm install Snippets`
2. The default action keyword is `sp` by default and it's recommended to replace it into `*` so that all the keys of snippets can be triggered directly.
2. Some use examples:  
  - `sp test-key:test-value`: Save the `key=test-key` and `value=test-value` into the local sqlite3 db.
  - `sp test`: Search for the `key=test-key` and click the item or `Enter` to copy the snippets value into clipboard.

> Disclaimer: The key/value would be stored on **local only ** via sqlite3 db file `./snippets.db` under `%FlowLauncherPluginFolder%/Snippets/`
