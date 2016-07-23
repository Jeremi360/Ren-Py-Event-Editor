label EEout_start:
    scene bg start code
    developer "Hi! Welcome in Ren'Py Event Editor."
    scene bg start imgs
    developer "First put right images(png and jpg) to right folders:\n
            - backgrounds to 'game/images/bgs'\n
            - character sprites to 'game/images/charaters'\n
            - events images in 'game/images/events'"
    menu:
        "I done this already":
            scene bg start code
            developer "Now see Tutorial then 'Add New Event' and call it 'start'.\n
                    It will over write this file."
            jump EE_start

        "I will comeback later":
            pass

    return
