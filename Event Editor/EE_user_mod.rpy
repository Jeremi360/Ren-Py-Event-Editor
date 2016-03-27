## This is the code that you need to change to synchronize the Event Editor with your game.

# Before proceeding remember that all characters and images that you want to use must be declared somewhere;
# for example some images and bg have already been defined in the file "EE_example_def.rpy"

###################################################################################################
###################################################################################################
#
#       STEP 1: Characters images
#
###################################################################################################
###################################################################################################
#
# For each character you have to create a list with the names of all the pictures of that character.
# For example in this case there are the three picture already declared in the "EE_example_def.rpy"
#
# Delete the example list and write your owns.

init:
    $ eileen_expressions = ["eileen happy","eileen vhappy","eileen concerned"]


#################################
##      STEP 1 bis: Event images
#################################
# The Event images Menu is optional; it gives you the possibility to create one or more lists of fullscreen images that are not "backgrounds".
# This may be useful if you have many fullscreen images and you want to group them.
#
#
# To activate this Menu set the following variable to 1:
init:
    $ EV_menu_active = 0

# Here create the lists like you did before
#
init:
    $ EV_example_group = ['black']



###################################################################################################
###################################################################################################
#
#       STEP 2: SCREENS
#
###################################################################################################
###################################################################################################
#
# The seguent menus are opened during the Event Editor session.
#
# You need to manually add the textbutton for every option you want.

###########################
##      Speaker
###########################
# In this menu you can choose who is talking (the name that will be shown above the speech text).
# NOTE: remember that the "color" option is mandatory when defining a character (see "EE_example_def.rpy"), otherwise the Event Editor will crash.

screen speaker_selection:
    zorder 1
    tag sc
    vbox:
        ymaximum 400
        box_wrap True
        yalign 0.3
        xalign 0.5

        # CUSTOMIZABLE SECTION ###################################################################
        # add one textbutton for each possibile character (defined somewhere else)
        #
        # textbutton _(<CHANGE_THIS>) action SetVariable('speaker_temp',<CHANGE_THIS>) xminimum 200
        #       <CUSTOM_1>: is the name you want to show on the button
        #       <CUSTOM_2>: is the name of the tag for the speaking character
        #
        textbutton _("None") action SetVariable('speaker_temp',"narrator") xminimum 200
        textbutton _("Eileen") action SetVariable('speaker_temp','e') xminimum 200
        # CUSTOMIZABLE SECTION END ###############################################################

        textbutton _("WRITE NEW") action ui.callsinnewcontext('insert_speaker_manually') xminimum 200
    textbutton _("DONE") yalign 0.3 xalign 1.0 action Hide('speaker_selection') xminimum 200


###########################
##      Background
###########################
# In this menu you can choose the background image.


screen BG_selection:
    zorder 1
    tag sc
    side "c r":
        area (5,0,490,455)
        viewport id "bg_sel":
            draggable True mousewheel True
            vbox:
                yalign 300
                xalign 400

                # CUSTOMIZABLE SECTION ###################################################################
                # add one textbutton for each possibile BG (defined somewhere else)
                #
                # textbutton _(<CUSTOM_1>) action SetVariable("BG_temp",<CUSTOM_2>) xminimum 150
                #       <CUSTOM_1>: is the name you want to show on the button
                #       <CUSTOM_2>: is the name of the image you want to show

                textbutton _("black") action SetVariable("BG_temp","black") xminimum 150

                #make buttons for all bgs
                for name in bgslist:
                    textbutton _(name) action SetVariable("BG_temp", name)  xminimum 150

                # CUSTOMIZABLE SECTION END ###############################################################

    textbutton _("DONE") yalign 0.3 xalign 1.0 action Hide('BG_selection') xminimum 200
    vbar value YScrollValue("bg_sel")



###########################
##      Background
###########################
# In this menu you can choose character shown on the screen.

screen character_selection:
    zorder 1
    tag sc

    textbutton _("DONE") yalign 0.5 xalign 0.95 action Hide('character_selection') xminimum 150
    vbox:
        yalign 0.15
        xfill True
        hbox:
            xfill True
            textbutton ("Char 1") action SetVariable('char_nu_temp',0) xminimum 150
            textbutton ("Char 2") action SetVariable('char_nu_temp',1) xminimum 150
            textbutton ("Char 3") action SetVariable('char_nu_temp',2) xminimum 150
        null height 10
        showif char_nu_temp == 0:
            hbox:
                xfill True
                textbutton ("left") action SetVariable('position_temp_char0',0)
                textbutton ("0.1") action SetVariable('position_temp_char0',0.1)
                textbutton ("0.2") action SetVariable('position_temp_char0',0.2)
                textbutton ("0.3") action SetVariable('position_temp_char0',0.3)
                textbutton ("0.4") action SetVariable('position_temp_char0',0.4)
                textbutton ("center") action SetVariable('position_temp_char0',0.5)
                textbutton ("0.6") action SetVariable('position_temp_char0',0.6)
                textbutton ("0.7") action SetVariable('position_temp_char0',0.7)
                textbutton ("0.8") action SetVariable('position_temp_char0',0.8)
                textbutton ("0.9") action SetVariable('position_temp_char0',0.9)
                textbutton ("right") action SetVariable('position_temp_char0',1.0)
            bar value VariableValue('position_temp_char0',1.6,offset=-0.3)
        elif char_nu_temp == 1:
            hbox:
                xfill True
                textbutton ("left") action SetVariable('position_temp_char1',0)
                textbutton ("0.1") action SetVariable('position_temp_char1',0.1)
                textbutton ("0.2") action SetVariable('position_temp_char1',0.2)
                textbutton ("0.3") action SetVariable('position_temp_char1',0.3)
                textbutton ("0.4") action SetVariable('position_temp_char1',0.4)
                textbutton ("center") action SetVariable('position_temp_char1',0.5)
                textbutton ("0.6") action SetVariable('position_temp_char1',0.6)
                textbutton ("0.7") action SetVariable('position_temp_char1',0.7)
                textbutton ("0.8") action SetVariable('position_temp_char1',0.8)
                textbutton ("0.9") action SetVariable('position_temp_char1',0.9)
                textbutton ("right") action SetVariable('position_temp_char1',1.0)
            bar value VariableValue('position_temp_char1',1.6,offset=-0.3)
        elif char_nu_temp == 2:
            hbox:
                xfill True
                textbutton ("left") action SetVariable('position_temp_char2',0)
                textbutton ("0.1") action SetVariable('position_temp_char2',0.1)
                textbutton ("0.2") action SetVariable('position_temp_char2',0.2)
                textbutton ("0.3") action SetVariable('position_temp_char2',0.3)
                textbutton ("0.4") action SetVariable('position_temp_char2',0.4)
                textbutton ("center") action SetVariable('position_temp_char2',0.5)
                textbutton ("0.6") action SetVariable('position_temp_char2',0.6)
                textbutton ("0.7") action SetVariable('position_temp_char2',0.7)
                textbutton ("0.8") action SetVariable('position_temp_char2',0.8)
                textbutton ("0.9") action SetVariable('position_temp_char2',0.9)
                textbutton ("right") action SetVariable('position_temp_char2',1.0)
            bar value VariableValue('position_temp_char2',1.6,offset=-0.3)
        textbutton ('[position_temp_char%s]'% char_nu_temp) action ui.callsinnewcontext('insert_pos_manually')

    hbox:
        yalign 0.6
        xalign 0.2
        spacing 10

        vbox:
            ymaximum 350
            box_wrap True
            yalign 0.5
            textbutton _("None") action [SetVariable('char_expressions',[""]),SetVariable("char_onscreen_temp%d" % char_nu_temp,'')] xminimum 200


            # CUSTOMIZABLE SECTION ###################################################################
            # add one textbutton for each possibile character
            #
            # textbutton _(<CUSTOM_1>) action SetVariable('char_expressions',<CUSTOM_2>) xminimum 150
            #       <CUSTOM_1>: is the name you want to show on the button
            #       <CUSTOM_2>: is the name of the list with the character images that you have created during the STEP 1 (above)
            #
            textbutton _("Eileen") action SetVariable('char_expressions',eileen_expressions) xminimum 150
            # CUSTOMIZABLE SECTION END ###############################################################

        vbox:
            yalign 0.5
            ymaximum 350
            box_wrap True
            for ii in range(len(char_expressions)):
                textbutton _("__%d__" % (ii+1)) action SetVariable("char_onscreen_temp%d" % char_nu_temp,char_expressions[ii]) xminimum 150



###########################
##      Event Images
###########################
# In this optional menu you can choose a fullscreen image to replace the background.
# NOTE: remember that this manu is inactive until you modify the variable EV_menu_active (above: STEP 1 bis)

screen EV_bg_selection:
    tag sc
    textbutton _("DONE") yalign 0.3 xalign 1.0 action Hide('EV_bg_selection')
    hbox:
        yalign 0.5
        vbox:
            yalign 0.5


            # CUSTOMIZABLE SECTION ###################################################################
            # add one textbutton for each group of fullscreen images
            #
            # textbutton _(<CUSTOM_1>) action SetVariable('EV_temp',<CUSTOM_2>) xminimum 200
            #       <CUSTOM_1>: is the name you want to show on the button
            #       <CUSTOM_2>: is the name of the list with the fulscreen images that you have created during the STEP 1 bis (above)
            #
            textbutton _("EV group 1") action SetVariable("EV_temp",EV_example_group) xminimum 200
            # CUSTOMIZABLE SECTION END ###############################################################

        vbox:
            ymaximum 400
            box_wrap True
            for ii in range(len(EV_temp)):
                textbutton _("__%d__" % (ii+1)) action SetVariable("BG_temp","%s" % EV_temp[ii]) xminimum 200
