
init -100:
    define bgs = []
    define ev_bgs = []
    define characters = []
    define speakers = []

    python:

        def addImgs(src, prefix, li):
            if file.startswith(src):
                if file.endswith('.png'):
                    name = file.replace(src, prefix)
                    name = name.replace('/', ' ')
                    name = name.replace('.png','')
                    renpy.image(name, Image(file))
                    li.append(name)

        for file in renpy.list_files():
            addImgs('images/bgs', 'bg', bgs)
            addImgs('images/events', 'event', ev_bgs)
            addImgs('images/characters', '', characters)


    image black = "#000"
