init -80 python:
    EE__label_list = renpy.get_all_labels()


label EE_test:
    scene bg start code

    developer "Here you can test yours events.\n
    If you don't see your event on list just restart game."

    label EE_watch_event_list_repeat:
        call screen EE_label_list
        call expression _return
        jump EE_test

    return


screen EE_label_list:

    vbox:
        xalign 0.5
        yalign 0.5
        box_wrap True
        for ii in EE__label_list:
            if "EEout_" in ii:
                textbutton _(ii) action Return(ii) xminimum 200
