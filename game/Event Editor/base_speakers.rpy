init -90 python:

    speakers = []

    base_speakers = {"boy":"#729fcf", "girl":"#e65fc8", "men":"#3465a4",
                    "women":"#ad7fa8", "devloper":"#cc0000", "debug":"#ef2920"}

    for sp in base_speakers.items():
        var_name = sp[0]
        ch_name = var_name.title().replace('_', ' ')
        xcolor =  sp[1]
        globals()[var_name] = Character(ch_name, color = xcolor)
        speakers.append(globals()[var_name])
