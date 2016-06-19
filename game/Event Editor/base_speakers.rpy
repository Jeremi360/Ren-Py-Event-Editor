init -90 python:

    speakers = []

    base_speakers = {"boy":"#729fcf", "girl":"#e65fc8", "men":"#3465a4",
                    "women":"#ad7fa8", "old men":"#555753",
                    "old women":"#d3d7cf", "devloper":"#cc0000", "debug":"#ef2920"}

    for sp in base_speakers.items():
        name = sp[0]
        xcolor =  sp[1]
        globals()[name] = Character(name, color = xcolor)
        speakers.append(name)
