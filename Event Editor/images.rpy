###############################################################
#Example for the pictures and character definition/declaration:
###############################################################

##The images declaration doesn't need any modification:

define bgslist = []
init python:

    for file in renpy.list_files():
        if file.startswith('images/bg'):
            if file.endswith('.png'):
                name = file.replace('images/bg','bg').replace('/', ' ').replace('.png','')
                renpy.image(name, Image(file, yanchor = config.screen_height))
                bgslist.append(name)

        if file.startswith('images/event'):
            if file.endswith('.png'):
                name = file.replace('images/event','event').replace('/', ' ').replace('.png','')
                renpy.image(name, Image(file, yanchor = config.screen_height))
                bgslist.append(name)

        if file.startswith('images/people'):
            if file.endswith('.png'):
                name = file.replace('images/people','').replace('/', ' ').replace('.png','')
                renpy.image(name, Image(file, yanchor = config.screen_height))
                bgslist.append(name)


image black = "#000"
