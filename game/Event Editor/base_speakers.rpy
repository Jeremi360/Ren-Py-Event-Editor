init -300 python:

    fs = Character(None, kind=nvl)
    centered = Character(None, kind=nvl, what_xalign=0.5, what_yalign=0.5)

    speakers = {
                #"fs":fs,
                #"centered":centered
                }

    base_speakers = {
                    "boy":"#729fcf", "boy_1":"#729fcf", "boy_2":"#729fcf",
                    "boy_3":"#729fcf", "boys":"#729fcf", "girl":"#e65fc8",
                    "girl_1":"#e65fc8", "girl_2":"#e65fc8","girl_3":"#e65fc8",
                    "girls":"#e65fc8", "men":"#3465a4", "women":"#ad7fa8",
                    "developer":"#cc0000", "debug":"#ef2920"
                    }

    for sp in base_speakers.items():
        var_name = sp[0]
        ch_name = var_name.replace("_", " ")
        ch_name = ch_name.title()
        xcolor =  sp[1]
        globals()[var_name] = Character(ch_name, color = xcolor)
        speakers[var_name] = globals()[var_name]
