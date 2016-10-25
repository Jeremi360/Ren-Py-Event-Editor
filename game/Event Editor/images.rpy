init -300 python:
    bgs = []
    ev_bgs = []
    characters = []

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

    def addBGs(src, prefix = 'bg'):
        addImgs(src, prefix, bgs)

    def addEVs(src, prefix = 'event'):
        addImgs(src, prefix, ev_bgs)

    def addChs(src, prefix = ''):
        addImgs(src, prefix, characters)
