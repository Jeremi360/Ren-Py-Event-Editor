# Ren'Py Event Editor
![](game/gui/window_icon.png)

Ren'Py Event Editor forked from this: [Ren'Py Event Editor forum topic](http://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=24108#p374045)

## Features:
- Support to use as mod in any game(just ajust EE_config.rpy in Event Editor folder)
- Support for [DSE(Dating Sim Engine)](https://github.com/renpy/dse)
- Support for mods / custom scenarios - see files in *mods/test*
- You can test your events from menu
- All generated events have *EEout_* prefix:
  - Events from main plot have *EEout_main_* prefix
  - Events from mods have *EEout_mod_name_* prefix

- Genterate buttons for all spekers added to speakers list:

  ```
  $ speakers["my_character_name_in_code"] = my_character_name_in_code
  ```

- Easy add custom images folders:

  ```
  init -30 python:
    addBGs('my_custom_bgs', 'my_bg_prefix') #default prefix is 'bg'
    addEVs('my_custom_ev', 'my_ev_prefix') #default prefix is 'event'
    addChs('my_custom_ch')
    ```

## Changes:
- Now tutorial have screen shots
- Some fixes in gui
- Move gui to new renpy gui (Ren'Py v.6.99.11.1749)
- Finished develop support for [DSE(Dating Sim Engine)](https://github.com/renpy/dse)
- Add *EE_config.rpy* to show default Event Editor configuration
- Change way of adding new speakers to fix bug
- Add test mod
- Fix indentation on speakers lines again
- Add Support for mods
- Add some new base colors
- Add imgs from Ren'Py Tutorial
- Remove buggy basic speakers
- Remove old comments
- Comments make in EE are in next line
- Fix indentation on speakers lines
- Added some basic speakers
- Added base bgs with black solid and Tango Palette  
- Automatic generate buttons for all images stored placed in *game/images*:
  - now png and jpg are supported
  - *game/images/characters* for charaters sprites
  - *game/images/bgs* for backgrounds
  - *game/images/events* for events
- Save your events to *game/events*
- All list are scrollable
