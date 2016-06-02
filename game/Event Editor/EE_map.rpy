####### DO NO CHANGE THIS CODE #######


init:
    $ EV_temp = []
    $ project_kind=""
    $ minievent_temp =""
    $ minievent_temp_a =""
    $ n_temp=0
    $ minievent_list ={}
    $ minievent_list['beginning']=minievent('beginning','beginning',False)


#################################

init -2:
    define narrator = Character('', color="#fff")

init -2 python:

    class minievent:
        def __init__(self,name,parent,branch=False,type='normal',branch_end=False,branching_text=''):
            self.name=name
            self.branch=branch
            self.parent=parent
            self.type=type
            self.branch_end=branch_end
            self.branching_text=branching_text

            self.totalpages=1
            self.speaker=['narrator','narrator']
            self.page_text= ["",""]
            self.BG = ["","black"]
            self.char_onscreen=[["","",""],["","",""]]
            self.char_position = [[0,0,0],[0,0,0]]
            self.comments=["",""]


    class event_branch:
        def __init__(self,name,parent,branch=False,type='branch',branch_end=False,branching_text=['']):
            self.name=name
            self.branch=branch
            self.parent=parent
            self.type=type
            self.branch_end=branch_end
            self.branching_text=branching_text


    def map_creator(minievent_info):
        ui.hbox(id="hbox "+minievent_info[0],yalign=0.5,xalign=0.5)
        ui.null(width=20)
        for ii in range(len(minievent_info)):
            if isinstance(minievent_list[minievent_info[ii]],event_branch):
                ui.frame(id="frame "+minievent_info[ii])
                ui.vbox(id="vbox "+minievent_info[ii],yalign=0.5,xalign=0.5)
                ui.textbutton(minievent_list[minievent_info[ii]].name+" BRANCH",clicked=[Show("minievent_menu_branch"),SetVariable('minievent_temp',minievent_list[minievent_info[ii]])],xalign=0.5,background='#FE9A2E')
                ui.null(height=30)
                map_creator(minievent_list[minievent_info[ii]].branch)

                if minievent_list[minievent_info[ii]].branch_end!=False:
                    ui.null(height=30)
                    map_creator(minievent_list[minievent_info[ii]].branch_end)
                ui.close()

            else:
                ui.vbox(id="vbox "+minievent_info[ii],yalign=0.5,xalign=0.5)
                ui.textbutton(minievent_list[minievent_info[ii]].name,clicked=[Show("minievent_menu_normal"),SetVariable('minievent_temp',minievent_list[minievent_info[ii]])],yalign=0.5,xalign=0.5)
                ui.null(height=30)
                if minievent_list[minievent_info[ii]].branch!=False:
                    map_creator(minievent_list[minievent_info[ii]].branch)
                ui.close()
            ui.null(width=20)
        ui.close()

    renpy.define_screen("map", map_creator)


###################################################################################################
###################################################################################################
#
#screens
#
###################################################################################################
###################################################################################################




label EE_map:
    $ minievent_list ={}
    $ minievent_list['beginning']=minievent('beginning','beginning',False)
    label EE_map_repeat:
    call screen sequence_map
    jump EE_map_repeat

screen sequence_map:
    imagemap:
        ground "#F6CEF5"
    viewport:
        draggable True
        mousewheel True
        $ map_creator(["beginning"])
    textbutton _("Map Menu") action ShowMenu("project_main_menu") xalign 1.0

screen project_main_menu:
    imagemap:
        ground "#2E64FE"

    textbutton _("BACK") action Return() xminimum 200 xalign 1.0
    vbox:
        text _("Event name: [project_name]") size 40
        null height 80
        textbutton _("Change Event Name") action ui.callsinnewcontext('change_project_name') xminimum 400
        textbutton _("Export Event") action Jump("exporting_project") xminimum 400
        null height 80
        textbutton _("Tutorial") action  Jump("EE_tutorial")



screen minievent_menu_normal:

    zorder 1
    tag sc
    frame:
        background "#fff"
        xalign 1.0
        yalign 0.5
        vbox:
            textbutton _("OPEN minievent") action [Hide('minievent_menu_normal'),Hide('sequence_map'),Jump('open_minievent')] xminimum 200
            textbutton _("ADD Branch") action If(minievent_temp.branch==False,[Hide('minievent_menu_normal'),Jump("add_branch")]) xminimum 200
            null height 80
            textbutton _("CLOSE window") action Hide("minievent_menu_normal") xminimum 200


label open_minievent:
    scene
    hide screen sequence_map
    $ page=1
    $ pagechange = 0
    $ sel_act=""
    $ BG_temp = "black"
    $ speaker_temp='narrator'
    $ c_position="0"
    $ char_expressions=[""]
    $ char_onscreen_temp0=""
    $ char_onscreen_temp1=""
    $ char_onscreen_temp2=""
    $ char_nu_temp = 0
    $ position_temp_char0= 0
    $ position_temp_char1= 0
    $ position_temp_char2= 0
    jump event_editor



label add_branch:
    $ name_temp=renpy.input("Write a name:")
    if name_temp=="" or name_temp in minievent_list:
        "Name not valid. Choose another one."
        jump add_branch
    $ minievent_list[name_temp]=event_branch(name_temp,minievent_temp.name,[name_temp+" choice1",name_temp+" choice2"],"branch",branching_text=["choice text","choice text"])
    $ minievent_list[name_temp+" choice1"]=minievent(name_temp+" choice1",name_temp+" MENU",False)
    $ minievent_list[name_temp+" choice2"]=minievent(name_temp+" choice2",name_temp+" MENU",False)
    $ minievent_temp.branch=[name_temp]
    jump EE_map_repeat



screen minievent_menu_branch:
    zorder 1
    tag sc

    imagemap:
        ground "#2E64FE"

    textbutton _("CLOSE") action [Hide("minievent_menu_branch"),Jump('EE_map_repeat')] xminimum 200 xalign 1.0
    vbox:
        text _("Branch options:") size 40
        null height 80
        text _("If you want all the branches to have the same ending, use the this option:")
        if minievent_temp.branch_end==False:
            textbutton _("ADD common minievent at the end") action [Hide("minievent_menu_branch"),Jump("add_end_branch")] xminimum 200
        else:
            textbutton _("DELETE common minievent at the end") action [Hide("minievent_menu_branch"),Jump("delete_end_branch")] xminimum 200

        #textbutton _("Rename branch") action [ShowMenu("rename_choice"),Hide("minievent_menu_branch")] xminimum 200
        null height 80
        hbox:
            xalign 0.5
            textbutton _("Add choice") action Jump("add_choice") xminimum 200
            null width 30
            textbutton _("Delete choice") action If(minievent_temp_a in minievent_temp.branch,Jump("delete_choice")) xminimum 200
            null width 30
            textbutton _("Change choice text") action If(minievent_temp_a in minievent_temp.branch,ui.callsinnewcontext("change_choice_text")) xminimum 200


        null height 80
        for ii in range(len(minievent_temp.branch)):
            hbox:
                textbutton _(minievent_temp.branch[ii]) action [SetVariable('minievent_temp_a',minievent_temp.branch[ii]),SetVariable("n_temp",ii)] xminimum 200
                null width 30
                text minievent_temp.branching_text[ii]


label add_choice:
    $ name_temp=minievent_temp.name+" choice"+str(len(minievent_temp.branch)+1)
    $ minievent_list[name_temp]=minievent(name_temp,minievent_temp.name,False)
    $ minievent_temp.branch.append(name_temp)
    $ minievent_temp.branching_text.append("choice text")
    jump EE_map_repeat



label add_end_branch:
    $ minievent_list[minievent_temp.name+" BRANCH \n common END"]=minievent(minievent_temp.name+" BRANCH \n common END",minievent_temp.name,False)
    $ minievent_temp.branch_end=[minievent_temp.name+" BRANCH \n common END"]
    jump EE_map_repeat


label delete_end_branch:
    hide screen minievent_menu_branch
    if minievent_list[minievent_temp.name+" BRANCH \n common END"].branch!=False:
        'You can\'t delete this choice. It still has some child events. You must delete them before you can delete this one.'
    else:
        menu:
            'are your sure you want to DELETE the common end event?'

            'YES':
                $ minievent_temp.branch_end=False
                $ del minievent_list[minievent_temp.name+" BRANCH \n common END"]

            'NO':
                pass
    jump EE_map_repeat


label delete_choice:
    hide screen sequence_map
    if minievent_list[minievent_temp_a].branch!=False:
        hide screen minievent_menu_branch
        'You can\'t delete this choice. It still has some child events. You must delete them before you can delete this one.'
    else:
        if len(minievent_temp.branch)==1:
            hide screen minievent_menu_branch
            'Only one choice remains.'
            'If you proceed the branch will be deleted.'
            menu:
                'Continue?'
                'Yes':
                    $ del minievent_list[minievent_temp_a]
                    $ minievent_list[minievent_temp.parent].branch=False
                    $ del minievent_list[minievent_temp.name]
                'No':
                    jump EE_map_repeat
        else:
            python:
                del minievent_temp.branch[n_temp]
                del minievent_temp.branching_text[n_temp]
                for ii in range(len(minievent_temp.branch)):
                    if ii==len(minievent_temp.branch)-1:
                        del minievent_list[minievent_temp.name+" choice"+str(ii+1)]
                    elif ii>=n_temp:
                        minievent_list[minievent_temp.name+" choice"+str(ii+1)]=minievent_list[minievent_temp.branch[ii]]
                        minievent_list[minievent_temp.name+" choice"+str(ii+1)].name=minievent_temp.name+" choice"+str(ii+1)
                        minievent_temp.branch[ii]= minievent_temp.name+" choice"+str(ii+1)
    jump EE_map_repeat




label change_choice_text:
     $ minievent_temp.branching_text[n_temp] = renpy.input("Change the choice text:",default=minievent_temp.branching_text[n_temp])
     jump EE_map_repeat
