label EE_tutorial:
    scene bg tutorial TexTOrNull

    "In the Event Editor each 'page' correspond to 'one click' in game."

    "VERY IMPORTANT:
        The editor does not notice that you have modified a page until you
        'change page'. So when you are going to EXPORT or SAVE the event, you
        should change page before doing so, this way you can be sure that your
         modifications are remembered."

    'TEXT' "When you start the Event Editor you will have the possibility
        to write the text that you want to show in this window you are reading now.
        You can input the text in this very same window. It can be both dialogue or
        narration text. There are just a a couple thing you have to remember."

    'TEXT' "You cannot write on a newline in the Event Editor.
        To do that you have to write '\\ n' (without the space in the middle) :
        when the event is shown in game, the text after '\\ n' will be shown on a new line."

    'TEXT' "\nAlso remember that there is no need of space after the n: 'Hi. \\ nHow are you?''.
        No space between '\\ n' and 'How'."

    scene bg tutorial SpeakerYou
    'SPEAKER' "Select this button in the top-left part of the screen to
        choose wich name will be shown as the 'speaker' of dialogue line.
        Select 'None' if you are going to write a narration text.
        \nAnd there is also a 'WRITE NEW' option to let you use a name that is
        not in 'speakers' list."

    scene bg tutorial BG
    'BACKGROUND' "Select the 'BG', 'BG Base' or 'Event BG' button and you will
                have the list of background options."

    scene bg tutorial Char
    'CHARACTER' "Select this to show some character on the screen.
        You can manage a max of three character on the screen at the same time.
        They will be 'char1', 'char2' and 'char3'."

    'CHARACTER' "Use the bar or the numbered buttons to decide the character\'s horizontal position.
        You can also press the button under the bar, on the left, to input the position yourself
         (it must be a number between 0 and 1)"

    'CHARACTER' "Under the position bar you will see some buttons with names on them.
        Choose wich character you want to display on the screen. On the right there will be
         other buttons with numbers: each number corrispond to a different face expression,
          body position or dress for the selected character."

    scene bg tutorial Comment
    'COMMENTS' "This open a new screen.
        In this screen you can add a comment for the page you were working on (you can also delete it).
        The comment will also be present in the EXPORTED code,
        after a \# so that anyone can see that comment when working on the code."

    'COMMENTS' "Also from this screen you can see all the comments of the current event.
        Use this option to remind yourself something or to give some info to anyone
         that will work on the exported code."

    scene bg tutorial Menu
    'MENU' "This button is in the top-right part of the screen.
        In this menu there are other option to modify your event."

    'EXPORT EVENT' "Very easy to use. Just push the button.
     Then, in the events folder if you make main plot or in mods/mod_name if you made for mod,
     you will find a file named EEout_mod_name/main_<project_name>.rpy.
      \nThat is the code for your event."

    scene bg tutorial SaveAndLoad
    'SAVE&LOAD' "If you want to save your work, you can do so with the
     normal SAVE system. Just press 'ESC', you will enter the game main menu
      and here you can save as if you were simply playing the game.
       To LOAD and contiue modifing your event just use the LOAD option."

    return
