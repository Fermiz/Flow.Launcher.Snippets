# Flow.Launcher.Snippets

This Snippets plugin let you save key/value snippets and copy to clipboard copy it from [Flow Launcher](https://www.flowlauncher.com/).

## How to use it

1. Install this plugin via `pm install Snippets`
2. The default action keyword is `sp` by default and it's recommended to replace it into `*` so that all the keys of snippets can be triggered directly.
2. Examples:  
  - **Save `<key>:<value>` for Single Line**: open FlowLauncher to type `sp <test-key>:<test-value>`, click or `Enter` the shown option `Save Code Snippets` to save the `key=test-key` and `value=test-value` into the local sqlite3 db.
  - **Save From Clipbaord for Multiple Line**: Copy your selected snippets and then open FlowLauncher to type `sp <clipboard-snippet-key>`, As `key=clipboard-snippet-key` is not saved yet and there are snippets from clipboard, click or `Enter` the shown option `Save from clipboard` to save the `key=clipboard-snippet-key` and `value=clipboard-snippets` into the local sqlite3 db.
  - **Get Snippets By Key**: `sp <test-key>`: Search for the `key=test-key` and click the item or `Enter` to copy the snippets value into clipboard.
  - **Delete Snippets By Key**: `sp <test-key>`: Search for the `key=test-key`, it would show the save item, press `Shift + Enter` to see the context menu on selected item, click the item or `Enter` to delet the snippets

> Disclaimer: The key/value would be stored on **local only ** via sqlite3 db file `./snippets.db` under `%FlowLauncherSettingsFolder%/Flow.Launcher.Snippets/`
