# Goto Definition Split

A goto definition side-by-side in a group instead of tab for Sublime Text.

**Overrides the built-in command so that the side-by-side is in a group instead of a tab.**

## Installation

Install [GotoDefinitionSplit](https://packagecontrol.io/packages/GotoDefinitionSplit) via Package Control.

**Install dependencies via Package Control.**

- [Origami](https://packagecontrol.io/packages/Origami)

## Key Bindings

Key  | OS   | Description
:--- | :--- | :----------
<kbd>CTRL+f12</kbd> | Linux | Goto definition in side by side group.
<kbd>SUPER+f12</kbd> | OSX | Goto definition in side by side group.
<kbd>CTRL+f12</kbd> | Windows | Goto definition in side by side group.

## NeoVintageous

If you use [NeoVintageous](https://packagecontrol.io/packages/NeoVintageous) you need to disable the <kbd>CTRL-F12</kbd>.

Menu → Preferences → Settings

```js
"vintageous_handle_keys":
{
    "<C-f12>": false,
},
```

Read the [neovintageous key handler](https://blog.gerardroche.com/2022/09/22/neovintageous-key-handler/) for a short guide on how the key handler works.



## License

Released under the [GPL-3.0-or-later License](LICENSE).
