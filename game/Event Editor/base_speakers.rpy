init -300 python:

    speakers = []

    base_speakers = {
                    "boy":"#729fcf", "boy1":"#729fcf", "boy2":"#729fcf",
                    "boy3":"#729fcf", "girl":"#e65fc8", "girl1":"#e65fc8",
                    "girl2":"#e65fc8","girl3":"#e65fc8",
                    "men":"#3465a4", "women":"#ad7fa8",
                    "developer":"#cc0000", "debug":"#ef2920"
                    }

    for sp in base_speakers.items():
        var_name = sp[0]
        ch_name = var_name.title()
        xcolor =  sp[1]
        globals()[var_name] = Character(ch_name, color = xcolor)
        speakers.append(globals()[var_name])
