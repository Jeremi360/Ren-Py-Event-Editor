## This is the code automatic synchronize the Event Editor with your game.
## Just put images in right folders:
##    - backgrounds to 'game/images/bgs'\n
##    - character sprites to 'game/images/charaters'\n
##    - events images in 'game/images/events'"
##
## And add every character to speakers list:
## $ speakers.append(mycharacter)
## To add custom image folder write in init -30 python:
## addBGs('my_custom_bgs_dir', 'my_bg_prefix') #you don't have to write prefix
## addEVs('my_custom_evs_dir', 'my_ev_prefix')
## addChs('my_custom_chs_dir')

screen speaker_selection:
    zorder 1
    tag sc
    side "c r":
        area (5, 100, 1260, 400)
        viewport id "bg_sel":
            draggable True mousewheel True
            vbox:
                ymaximum 600
                box_wrap True
                yalign 0.3
                xalign 0.5

                textbutton _("None") action SetVariable('speaker_temp',"") xminimum 200

                for s in speakers.items():

                    if s[1].name == None:
                        $n = s[0].title()

                    else:
                        $n = s[1].name

                    $call_speaker = s[0]

                    textbutton _(n) action SetVariable('speaker_temp', call_speaker) xminimum 200

                textbutton _("WRITE NEW") action ui.callsinnewcontext('insert_speaker_manually') xminimum 200
    textbutton _("DONE") yalign 0.3 xalign 1.0 action Hide('speaker_selection') xminimum 200


screen BG_selection:
    zorder 1
    tag sc
    side "c r":
        area (5, 100, 1260, 400)
        viewport id "bg_sel":
            draggable True mousewheel True
            vbox:
                yalign 300
                xalign 400

                for name in bgs:
                    textbutton _(name) action SetVariable("BG_temp", name)  xminimum 150

    textbutton _("DONE") yalign 0.3 xalign 1.0 action Hide('BG_selection') xminimum 200
    vbar value YScrollValue("bg_sel")


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


    side "c r":
        area (5, 250, 1260, 300)
        viewport id "char_sel":
            draggable True mousewheel True

            vbox:
                yalign 0.6
                xalign 0.2
                spacing 10

                textbutton _("None") action [SetVariable('char_expressions',[""]),
                                            SetVariable("char_onscreen_temp%d" % char_nu_temp,'')] xminimum 200

                for name in characters:
                    textbutton _(name) action [SetVariable('char_expressions', name),
                                                SetVariable("char_onscreen_temp%d" % char_nu_temp, name)] xminimum 150


screen EV_bg_selection:
    tag sc
    zorder 1
    side "c r":
        area (5, 100, 1260, 400)
        viewport id "ev_bg_sel":
            draggable True mousewheel True

            hbox:
                yalign 0.5
                vbox:
                    yalign 0.5

                    for name in ev_bgs:
                        textbutton _(name) action SetVariable("BG_temp", name)  xminimum 150

    textbutton _("DONE") yalign 0.3 xalign 1.0 action Hide('EV_bg_selection')
    vbar value YScrollValue("ev_bg_sel")


screen BG_base_selection:
    zorder 1
    tag sc
    side "c r":
        area (5, 100, 1260, 400)
        viewport id "bg_base_sel":
            draggable True mousewheel True
            vbox:
                yalign 300
                xalign 400

                for name in base_colors:
                    textbutton _(name) action SetVariable("BG_temp", name)  xminimum 150

                for name in tango:
                    textbutton _(name) action SetVariable("BG_temp", name)  xminimum 150

            textbutton _("DONE") yalign 0.3 xalign 1.0 action Hide('BG_base_selection') xminimum 200
            vbar value YScrollValue("bg_base_sel")
