init -300 python:

    base_colors_dir = {
                    "Red": "#ff0000",
                    "Blue": "#0500fc",
                    "Green": "#00ff12",
                    "White": "#ffffff",
                    "Black": "#000"
                    }

    base_colors = []
    for c in base_colors_dir.items():
        name = c[0]
        renpy.image(name, Solid(c[1]))
        base_colors.append(name)
