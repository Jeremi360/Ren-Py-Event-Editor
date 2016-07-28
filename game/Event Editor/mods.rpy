init -300:
    $ mods = {}

label mods_sec:
    scene bg start code

    developer "Here you can play custom scenarios or read about installed mods"

    label EE_mods_repeat:
        call screen mods_selection
        call expression _return
        jump mods_sec

    return

screen mods_selection:
    side "c b r":
        area (100, 100, 600, 400)
        viewport id "vp":
            draggable True
            mousewheel True

            vbox:
                box_wrap True
                yalign 0.5
                xalign 0.5

                for mod in mods.items():
                    $n = mod[0]
                    $mod_start = mod[1]
                    textbutton _(n) action Return(mod_start) xminimum 200
                    
            vbar value YScrollValue("vp")
