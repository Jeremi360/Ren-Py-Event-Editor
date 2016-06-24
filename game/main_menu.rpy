##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"

    # The main menu buttons.
    frame:
        style_group "mm"
        xalign .98
        yalign .98

        has vbox

        textbutton _("New Game") action Start()
        textbutton _("Add New Event") action Start("EE_start")
        textbutton _("Import ...") action Start("import_imgs")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit(confirm=False)

init -2:

    # Make all the main menu buttons be the same size.
    style mm_button:
        size_group "mm"

    python:
        import tkFileDialog as fd
        imgs = [("Ren'Py supported images types", "*.png *.jpg *.jpeg")]
        sprites = []


label import_imgs:
    scene bg start imgs
    menu:
        "Import Scene Backgrounds":
            python:
                fd.askopenfilename(filetypes=

                                    )
