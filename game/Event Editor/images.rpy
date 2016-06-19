
init -100:
    define bgs = []
    define ev_bgs = []
    define characters = []

    python:

        exts = ['.png', '.jpg']
        spaces = ['/', '_']

        def addImgs(src, prefix, li):
            for file in renpy.list_files():
                if file.startswith(src):
                    if file.endswith(tuple(exts)):
                        name = file.replace(src, prefix)

                        for space in spaces:
                            name = name.replace(space, ' ')

                        for ext in exts:
                            name = name.replace(ext,'')

                        renpy.image(name, Image(file))
                        li.append(name)

        #for file in renpy.list_files():
        addImgs('images/bgs', 'bg', bgs)
        addImgs('images/events', 'event', ev_bgs)
        addImgs('images/characters', '', characters)


    image black = "#000"
