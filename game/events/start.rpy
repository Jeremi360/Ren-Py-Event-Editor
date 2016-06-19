label start:
    scene bg start code
    devloper "Hi! Welcome in Ren'Py Event Editor."
    scene bg start imgs
    devloper "First put right images(png and jpg) to right folders:\n
            - backgrounds to 'game/images/bgs'\n
            - character sprites to 'game/images/charaters'\n
            - events images in 'game/images/events'"
    menu:
        "I done this already":
            scene bg start code
            devloper "Now see Tutorial then 'Add New Event' and call it 'start'.\n
                    It will over write this file."
            jump EE_start

        "I will comeback later":
            pass

    return
