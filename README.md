# Ren-Py-Event-Editor
Ren'Py Event Editor forked from this: [Ren'Py Event Editor 2.1.1 forum post][1]

#Now it:
- Automatic generate buttons for all images stored placed in *game/images*:
  - *game/images/bgs* for backgrounds
  - *game/images/envents* for events
  - *game/image/characters* for charaters sprites
- Save your events to *game/events*
- All list are scrollable
- Genterate buttons for all spekers added to speakers list


#To install in your game:
- Unpack it in your project *game* folder 
- Open *screen.rpy* file in your project *game* folder
- Find `screen main_menu:` block of code
- At end of it add `textbutton _("Event Editor") action Start(""EE_start")`

[1]:http://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=24108#p374045
