init -300 python:

    tango_base = {"Butter":("#fce94f", "#edd400", "#c4a000"),

                    "Orange":("#fcaf3e", "#f57900", "#ce5c00"),

                    "Chocolate":("#e9b96e", "#c17d11", "#8f5902"),

                    "Chameleon":("#8ae232", "#73d216", "#4e9a06"),

                    "Sky":("#729fcf", "#3465a4", "#204a87"),

                    "Plum":("#ad7fa8", "#75507b", "#5c3566"),

                    "Scarlet":("#ef2920", "#cc0000", "#a40000"),

                    "Aluminium":("#eeeeec", "#d3d7cf", "#babdb6",
                                "#888a85", "#555753", "#2e3436")}

    tango = []

    for c in tango_base.keys():
        i = 1

        for v in tango_base[c]:
            name = " ".join(["tango", c, str(i)])
            name = name.replace(' 1', '')
            renpy.image(name, Solid(v))
            tango.append(name)
            i += 1
