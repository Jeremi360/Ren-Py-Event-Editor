# Beta content for the DSE module of the Event Editor
#
#

init -20 python:
    class possible_condition():
        def __init__(self,textbutton_text,variable_name,variable_type='number'):
            self.textbutton_text = textbutton_text
            self.variable_name = variable_name
            self.variable_type = variable_type


    class condition_content():
        def __init__(self,condition_property,operator='==',variable_value='0'):
            self.condition_property = condition_property
            self.operator = operator
            self.variable_value = variable_value

    def EE__changecondition(num,num2):
        EE__conditions_used_list[num2].condition_property = EE__DES_possible_conditions_list[num]
        if EE__DES_possible_conditions_list[num].variable_type != 'number':
            EE__conditions_used_list[num2].operator = "=="

    def EE__changeoperator(num,str):
        EE__conditions_used_list[num].operator=str

    def EE__remove_condition(num):
        del EE__conditions_used_list[num]


###################################################################################################
###################################################################################################
#
#       STEP 3: DSE CONDITIONS (optional)
#
###################################################################################################
###################################################################################################


init python:
    EE__conditions_used_list = []
    EE__DSE_once = 0
    EE__DSE_group = 0


########################################################
#
# Screens for the DSE conditions
#
########################################################

screen EE__DSEmodule:
    imagemap:
        ground "#000"
    textbutton _('BACK') action Return() xalign 1.0
    vbox:
        text _("DSE module") size 40
        null height 50
        hbox:
            text _("Event will appear only once")
            null width 50
            showif EE__DSE_once==0:
                textbutton _("Off") action SetVariable("EE__DSE_once",1)
            else:
                textbutton _("On") action SetVariable("EE__DSE_once",0)
        null height 20
        hbox:
            text _("Event is in group")
            null width 50
            showif EE__DSE_group==0:
                textbutton _("No group") action Show('EE__DSE_choose_group_screen')
            else:
                textbutton _('[EE__DSE_group]') action Show('EE__DSE_choose_group_screen')
        null height 80
        textbutton _('Add condition') action SetVariable("EE__conditions_used_list",EE__conditions_used_list+[condition_content(EE__DES_possible_conditions_list[0])]) xalign 0.5
        null height 40
        viewport:
            xsize 800
            xfill True
            scrollbars "vertical"
            mousewheel True
            vbox:
                xfill True
                spacing 10
                for ii in range(len(EE__conditions_used_list)):
                    hbox:
                        xfill True
                        textbutton _('Remove') action [Function(EE__remove_condition,ii),Show('EE__DSEmodule')]
                        null width 30
                        textbutton _(EE__conditions_used_list[ii].condition_property.textbutton_text) action Show("choose_condition_screen",[],ii)
                        textbutton ("%s" % EE__conditions_used_list[ii].operator) action Show("choose_operator_screen",[],ii) xalign 1.0
                        textbutton ("%s" % EE__conditions_used_list[ii].variable_value) action [Function(ui.callsinnewcontext("EE__choose_condition_value",EE__conditions_used_list[ii].variable_value,ii)),Show('EE__DSEmodule')] xalign 1.0




screen EE__DSE_choose_group_screen:
    tag EE__DSE_sel_screen
    vbox:
        xpos 0.75
        yalign 0.5
        textbutton _('No group') action [SetVariable('EE__DSE_group',0),Hide("EE__DSE_choose_group_screen")] xminimum 200
        for ii in range (len(EE__DSE_group_list)):
            textbutton _(EE__DSE_group_list[ii]) action [SetVariable('EE__DSE_group',EE__DSE_group_list[ii]),Hide("EE__DSE_choose_group_screen")] xminimum 200


screen choose_condition_screen(jj):
    tag EE__DSE_sel_screen
    vbox:
        xpos 0.75
        yalign 0.5
        for ii in range (len(EE__DES_possible_conditions_list)):
            textbutton _(EE__DES_possible_conditions_list[ii].textbutton_text) action [Function(EE__changecondition,ii,jj),Hide("choose_condition_screen")] xminimum 200


screen choose_operator_screen(num):
    tag EE__DSE_sel_screen
    vbox:
        xpos 0.75
        yalign 0.5
        textbutton _('== (equal to)') action [Function(EE__changeoperator,num,"=="),Hide('choose_operator_screen')] xminimum 200
        showif EE__conditions_used_list[num].condition_property.variable_type == 'number':
            textbutton _('!= (not equal to)') action [Function(EE__changeoperator,num,"!="),Hide('choose_operator_screen')] xminimum 200
            textbutton _('> (major than)') action [Function(EE__changeoperator,num,">"),Hide('choose_operator_screen')] xminimum 200
            textbutton _('>= (equal or major than)') action [Function(EE__changeoperator,num,">="),Hide('choose_operator_screen')] xminimum 200
            textbutton _('<(minor than)') action [Function(EE__changeoperator,num,"<"),Hide('choose_operator_screen')] xminimum 200
            textbutton _('<= (equal or minor than)') action [Function(EE__changeoperator,num,"<="),Hide('choose_operator_screen')] xminimum 200



label EE__choose_condition_value(out,num):
    scene black
    if EE__conditions_used_list[num].condition_property.variable_type == 'number':
        $ out = renpy.input("Write the value:",allow="0123456789")
        if out=="":
            jump EE__choose_condition_value
        $ EE__conditions_used_list[num].variable_value = out
    elif EE__conditions_used_list[num].condition_property.variable_type == 'boolean':
        if EE__conditions_used_list[num].variable_value == "True":
            $ EE__conditions_used_list[num].variable_value = "False"
        else:
            $ EE__conditions_used_list[num].variable_value = "True"
        show screen EE__DSEmodule
    return
